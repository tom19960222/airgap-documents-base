# 索引建置加速實測

2026-09-17 在目前完整 corpus 比較修改前後的程式。相同語料共 35,291 頁、339,555,721 bytes，產生 300,450 個 chunks。環境是 macOS 15.7.9 x86_64、12 個 logical CPUs、Python 3.14.2、SQLite 3.43.2。舊版取自 `ce635e51` 的 `runtime/build_index.py`。

## 完整流程結果

先交錯測量新舊版本兩輪，再測量完成 FTS 調校的最後版本兩輪。下表保留舊版基準與最後版本的結果；新舊各自使用獨立 SQLite 檔案，每次 full 後再跑一次無變更增量。新版使用 `jobs=4`。未清除 OS 檔案快取，也未隔離系統背景負載；以下是本機實測，不能直接推估其他主機或網路掛載的時間。

| 情境 | 舊版第 1 輪 | 新版第 1 輪 | 舊版第 2 輪 | 新版第 2 輪 |
|---|---:|---:|---:|---:|
| 完整重建 | 41.187 秒 | 18.029 秒 | 41.422 秒 | 16.112 秒 |
| 無變更增量 | 8.127 秒 | 0.884 秒 | 8.827 秒 | 0.850 秒 |

以兩輪平均比較，完整重建約快 2.4 倍（省下 59% 時間），無變更增量約快 9.8 倍（省下 90% 時間）。新版完整重建的讀檔、雜湊、解析與寫入合計約 4.9–5.5 秒，FTS 建立及最終合併仍需 10.0–11.1 秒，是目前主要耗時。

強制逐頁 SHA-256 的 `--verify-content --jobs 4` 另測得 3.112 秒及 2.156 秒，兩次都讀取全部 35,291 頁且沒有重建任何 chunks。需要保留舊版逐檔雜湊行為時，也可享有平行讀取的改善。

## 保留的修改

- 以檔案大小、mtime、ctime、inode、device 組成 POSIX 狀態快取；未變更文件不再每次重讀及計算 SHA-256。原有 manifest 可原地補欄位，無須重建既有 chunks 或 FTS。
- `--verify-content` 強制逐頁 SHA-256；Windows 自動採用逐頁雜湊。低時間精度檔案系統或網路掛載應使用內容驗證。
- CLI 預設最多 4 個解析程序，按 32 頁分批，每個程序最多預送兩批；主程序依原有頁面順序寫入 SQLite。新增與修改大量文件也適用；少量變更會縮減 worker 數量。
- 每頁 chunks 透過 `executemany` 寫入，重複標題使用持續遞增的序號，並先排除不可能是 heading 的行。
- 全量 FTS 建立時暫時延後自動 segment merge，完成後統一 `optimize`，再恢復預設 `automerge=4`、`crisismerge=16`，讓後續增量更新正常運作。
- 保留 SQLite transaction rollback、同目錄暫存檔與成功後 atomic replace；沒有關閉 journal 或 synchronous。

重複標題測例中，1,002 個 sections 的 slug 呼叫由 502,502 次降到 1,002 次。初步全語料純解析對照由 10.790 秒降到 6.484 秒；此數字排除讀檔與 SQLite，不能當成完整重建時間。

## 調校比較

初步完整語料原型中，2／4／8 個 processes 分別約 20.8／17.2／16.6 秒；4／8 個 threads 則約 26.8／27.6 秒。8 個 processes 的額外收益有限，因此預設最多 4 個，仍提供 `--jobs` 自行調整。

kernel 子語料的 SQLite cache 64 MiB 與延後建立一般索引測試，整體差異不到 0.2 秒；完整語料的延後一般索引原型約 17.7 秒，仍落在未調校 FTS 的 17.2–19.3 秒範圍，沒有足夠收益支持增加預設記憶體用量或更動 chunks schema。

完整語料的延後 FTS merge 原型約 14.9 秒，改大 FTS block 為 16 KiB 約 15.7 秒。採用前者並重測後得到表中的 16.1–18.0 秒；保留原本 FTS block 大小。單次原型時間只用於選擇方向，不當作最終加速宣稱。

## 驗證方式

21 個回歸測試全部通過，包含增量與全量一致、同大小且同 mtime 改寫、inode 替換、舊 manifest 升級、強制內容驗證、平行解析順序，以及 worker／寫入／FTS 失敗後的回復。

另外針對完整語料驗證：

- 新舊資料庫的 300,450 筆 chunks（包含 rowid、chunk ID、完整內容與 metadata）逐筆完全相同。
- 35,291 筆 page path、SHA-256、chunk count 逐筆完全相同。
- SQLite `integrity_check` 與 FTS5 external-content `integrity-check` 均通過。
- 12 組跨 Ceph、Rook、Cilium、KubeVirt、NetBox、GitLab、kernel、QEMU、Svelte 的搜尋，每組前 20 筆結果、分數與摘要均相同；collections 統計也相同。

回歸測試命令：

```bash
python3 -m unittest discover -s runtime/tests -v
```

效能重現方式：從舊 commit 匯出程式，將新舊模組的 `build_index(corpus, target_db, full=True)` 依序執行；新版傳入 `jobs=4`，之後用相同資料庫執行增量。呼叫必須放在 Python 檔案的 `if __name__ == '__main__':` 內，讓 multiprocessing 能安全啟動。使用各自獨立的 target_db，計時使用回傳的 `total_seconds`，避免只比較其中一個階段。

程式的 `scan_seconds` 現在只計算目錄與檔案狀態掃描；平行讀檔、雜湊及解析與主程序寫入互相重疊，合併計入 `update_seconds`。比較新舊效能時，應以完整耗時為準。

## 參考

SQLite 的 [FTS5 merge、rebuild 與 integrity-check 說明](https://www.sqlite.org/fts5.html#special_insert_commands) 與 [PRAGMA cache_size](https://www.sqlite.org/pragma.html#pragma_cache_size) 用於確認調校選項；[journal_mode](https://www.sqlite.org/pragma.html#pragma_journal_mode) 說明關閉 journal 會失去 rollback 能力，因此本次保留既有交易設定。
