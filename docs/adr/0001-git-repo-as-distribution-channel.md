# 用 git repo 當語料搬運管道，而非簽章 bundle

專案名稱暗示 air-gap，但實際環境是「出站受限、可從 GitHub pull」。因此語料以本 repo（Corpus Repo）承載，air-gap 端用 `git pull` 取得與更新——完整性驗證與 delta 更新由 git 免費提供，不另做 tar bundle、簽章、rollback 機制。代價是 repo 只能放純文字：FTS5 索引等二進位產物不進 git，改由 air-gap 端 pull 後在本地以 `build-index` 重建。

## Considered Options

- 簽章 tar.zst bundle（GPT 建議的正式產品做法）：適合完全隔離環境，但在「可 git pull」的前提下是多餘的複雜度。
- FTS5 db 進 git（或 Git LFS）：pull 完即用，但二進位整檔重寫會讓 repo 快速膨脹，LFS 又多一個 mirror 相依條件。
