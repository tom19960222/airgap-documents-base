---
collection: opencode
version: "2.0.30"
title: "HTTP API"
source_url: https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/openapi.json
fetched_at: 2026-10-15T19:48:22Z
---
# HTTP API

## Overview

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "opencode HttpApi",
    "version": "0.0.1",
    "description": "Experimental HttpApi surface for selected instance routes."
  },
  "security": [],
  "tags": [
    {
      "name": "server"
    },
    {
      "name": "location"
    },
    {
      "name": "agent"
    },
    {
      "name": "plugin",
      "description": "Experimental plugin routes."
    },
    {
      "name": "session",
      "description": "Experimental session routes."
    },
    {
      "name": "session",
      "description": "Experimental message routes."
    },
    {
      "name": "model",
      "description": "Experimental model routes."
    },
    {
      "name": "generate",
      "description": "Experimental one-shot generation routes."
    },
    {
      "name": "provider",
      "description": "Experimental provider routes."
    },
    {
      "name": "integration",
      "description": "Integration discovery and authentication routes."
    },
    {
      "name": "mcp",
      "description": "MCP server and resource routes."
    },
    {
      "name": "credential"
    },
    {
      "name": "project",
      "description": "Project routes."
    },
    {
      "name": "form",
      "description": "Location form routes."
    },
    {
      "name": "permission",
      "description": "Experimental permission routes."
    },
    {
      "name": "filesystem",
      "description": "Experimental location-scoped filesystem routes."
    },
    {
      "name": "command",
      "description": "Experimental command routes."
    },
    {
      "name": "skill",
      "description": "Experimental skill routes."
    },
    {
      "name": "rpc",
      "description": "Plugin RPC routes."
    },
    {
      "name": "event",
      "description": "Experimental event stream routes."
    },
    {
      "name": "pty",
      "description": "Experimental location-scoped PTY routes."
    },
    {
      "name": "persistentPty",
      "description": "Prototype persistent PTY routes."
    },
    {
      "name": "shell",
      "description": "Location-scoped shell command routes."
    },
    {
      "name": "reference",
      "description": "Location-scoped project references."
    },
    {
      "name": "worktree",
      "description": "Project-based worktree management routes."
    },
    {
      "name": "vcs",
      "description": "Location-scoped version control routes."
    },
    {
      "name": "debug"
    },
    {
      "name": "migration"
    },
    {
      "name": "websearch",
      "description": "Location-scoped web search routes."
    },
    {
      "name": "config",
      "description": "Location-scoped configuration routes."
    }
  ]
}
```

## /api/info

<a id="server.info"></a>

### GET /api/info — server.info

```json
{
  "tags": [
    "server"
  ],
  "operationId": "server.info",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "ServerInfo",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServerInfo"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Return the server identity, connection URLs, paths, and readiness status.",
  "summary": "Get server info"
}
```

## /api/pair

<a id="server.pair"></a>

### POST /api/pair — server.pair

```json
{
  "tags": [
    "server"
  ],
  "operationId": "server.pair",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "PairingCode",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PairingCode"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Create a short-lived, single-use code for a /auth/connect/:code pairing link.",
  "summary": "Create pairing code"
}
```

## /auth/connect/{code}

<a id="server.connect"></a>

### GET /auth/connect/{code} — server.connect

```json
{
  "tags": [
    "server"
  ],
  "operationId": "server.connect",
  "parameters": [
    {
      "name": "code",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "PairingSession",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PairingSession"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Redeem a pairing code. Browsers receive a session cookie and a redirect to the web app; requests that accept JSON receive a session token to use as the password.",
  "summary": "Redeem pairing code"
}
```

## /api/location

<a id="location.get"></a>

### GET /api/location — location.get

```json
{
  "tags": [
    "location"
  ],
  "operationId": "location.get",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Location.PublicInfo",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/Location.PublicInfo"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Resolve the requested location or the server default location.",
  "summary": "Get location"
}
```

## /api/location/reload

<a id="location.reload"></a>

### POST /api/location/reload — location.reload

```json
{
  "tags": [
    "location"
  ],
  "operationId": "location.reload",
  "parameters": [],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Shut down and rebuild every loaded location. Pending permissions and forms are cancelled; running sessions continue with fresh services at the next step boundary. Emits location.shutdown for client recovery and responds once all replacement builds settle.",
  "summary": "Reload configuration"
}
```

## /api/agent

<a id="agent.list"></a>

### GET /api/agent — agent.list

```json
{
  "tags": [
    "agent"
  ],
  "operationId": "agent.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Agent.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve currently registered agents.",
  "summary": "List agents"
}
```

## /api/agent/{agentID}

<a id="agent.get"></a>

### GET /api/agent/{agentID} — agent.get

```json
{
  "tags": [
    "agent"
  ],
  "operationId": "agent.get",
  "parameters": [
    {
      "name": "agentID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Agent.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Agent.Info"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "AgentNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/AgentNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve a single currently registered agent.",
  "summary": "Get agent"
}
```

## /api/plugin

<a id="plugin.list"></a>

### GET /api/plugin — plugin.list

```json
{
  "tags": [
    "plugin"
  ],
  "operationId": "plugin.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Plugin.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve enabled server plugins and their current status.",
  "summary": "List plugins"
}
```

## /api/plugin/check

<a id="plugin.check"></a>

### POST /api/plugin/check — plugin.check

```json
{
  "tags": [
    "plugin"
  ],
  "operationId": "plugin.check",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Plugin.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Check one or all package plugins for available updates.",
  "summary": "Check plugin updates",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "target": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/plugin/update

<a id="plugin.update"></a>

### POST /api/plugin/update — plugin.update

```json
{
  "tags": [
    "plugin"
  ],
  "operationId": "plugin.update",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Update package plugins concurrently and notify active locations to reload them. Responds once every update has finished; fails when any update fails.",
  "summary": "Update plugins",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "targets": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "targets"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session

<a id="session.list"></a>

### GET /api/session — session.list

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.list",
  "parameters": [
    {
      "name": "limit",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Maximum number of sessions to return. Defaults to the newest 50 sessions."
      },
      "required": false
    },
    {
      "name": "order",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "type": "null"
          }
        ],
        "description": "Session order for the first page. Use desc for newest first or asc for oldest first."
      },
      "required": false
    },
    {
      "name": "search",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "parentID",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "anyOf": [
              {
                "$ref": "#/components/schemas/Session.ID"
              },
              {
                "type": "string",
                "enum": [
                  "null"
                ]
              }
            ],
            "description": "Filter by parent session. Use null to return only root sessions."
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "directory",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/AbsolutePath"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "project",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Project.ID"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "subpath",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/RelativePath"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "cursor",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/SessionsCursor"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "SessionsResponse",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionsResponse"
          }
        }
      }
    },
    "400": {
      "description": "InvalidCursorError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/InvalidCursorErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve sessions in the requested order. Items keep that order across pages; use cursor.next or cursor.previous to move through the ordered list.",
  "summary": "List sessions"
}
```

<a id="session.create"></a>

### POST /api/session — session.create

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.create",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Create a session at the requested location. A parentID creates a linked child session at its parent's location.",
  "summary": "Create session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "parentID": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "title": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            },
            "agent": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Agent.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "model": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Model.Ref"
                },
                {
                  "type": "null"
                }
              ]
            },
            "location": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Location.PublicRef"
                },
                {
                  "type": "null"
                }
              ]
            },
            "metadata": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Metadata"
                },
                {
                  "type": "null"
                }
              ]
            },
            "permissions": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Permission.Ruleset"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/session/stats

<a id="experimental.session.stats"></a>

### GET /api/experimental/session/stats — experimental.session.stats

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.stats",
  "parameters": [
    {
      "name": "from",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "to",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "project",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Project.ID"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "timezone",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "tools",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "none",
              "summary",
              "detail"
            ]
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/SessionStats.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Aggregate local session activity, usage, and tool reliability for a time range.",
  "summary": "Get session statistics"
}
```

## /api/experimental/session/import

<a id="experimental.session.import"></a>

### POST /api/experimental/session/import — experimental.session.import

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.import",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Import a projected session transcript at the requested location. If parentID is supplied, the parent session must already exist; import parents before children.",
  "summary": "Import session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "info": {
              "$ref": "#/components/schemas/Session.Info"
            },
            "messages": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Session.Message.Info"
              }
            },
            "location": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Location.PublicRef"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "info",
            "messages"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/session/{sessionID}/export

<a id="experimental.session.export"></a>

### GET /api/experimental/session/{sessionID}/export — experimental.session.export

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.export",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "sanitize",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "true",
              "false"
            ]
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/SessionTransfer.Data"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    },
    "500": {
      "description": "UnknownError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnknownErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Export a complete projected session transcript.",
  "summary": "Export session"
}
```

## /api/session/active

<a id="session.active"></a>

### GET /api/session/active — session.active

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.active",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "object",
                "patternProperties": {
                  "^ses": {
                    "$ref": "#/components/schemas/SessionActive"
                  }
                },
                "additionalProperties": false
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve foreground Session drains currently owned by this OpenCode process. Sessions absent from the result are inactive.",
  "summary": "List active sessions"
}
```

## /api/session/{sessionID}

<a id="session.get"></a>

### GET /api/session/{sessionID} — session.get

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.get",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve a session by ID.",
  "summary": "Get session"
}
```

<a id="session.remove"></a>

### DELETE /api/session/{sessionID} — session.remove

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.remove",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Delete a session and its child sessions.",
  "summary": "Delete session"
}
```

<a id="session.update"></a>

### PATCH /api/session/{sessionID} — session.update

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.update",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Update mutable session properties.",
  "summary": "Update session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "title": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            },
            "metadata": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Metadata"
                },
                {
                  "type": "null"
                }
              ]
            },
            "permissions": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Permission.Ruleset"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/fork

<a id="session.fork"></a>

### POST /api/session/{sessionID}/fork — session.fork

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.fork",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | MessageNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/MessageNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Create a child session by copying projected history before a message. Omit before to copy the full history.",
  "summary": "Fork session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "before": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Message.ID"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/agent

<a id="session.switchAgent"></a>

### POST /api/session/{sessionID}/agent — session.switchAgent

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.switchAgent",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Switch the agent used by subsequent provider turns.",
  "summary": "Switch session agent",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "agent": {
              "$ref": "#/components/schemas/Agent.ID"
            }
          },
          "required": [
            "agent"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/model

<a id="session.switchModel"></a>

### POST /api/session/{sessionID}/model — session.switchModel

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.switchModel",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Switch the model used by subsequent provider turns.",
  "summary": "Switch session model",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "model": {
              "$ref": "#/components/schemas/Model.Ref"
            }
          },
          "required": [
            "model"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/move

<a id="session.move"></a>

### POST /api/session/{sessionID}/move — session.move

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.move",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Move a session to another project directory at the requested delivery boundary.",
  "summary": "Move session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "directory": {
              "$ref": "#/components/schemas/AbsolutePath"
            },
            "delivery": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Inbox.Delivery"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "directory"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/prompt

<a id="session.prompt"></a>

### POST /api/session/{sessionID}/prompt — session.prompt

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.prompt",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Inbox.User"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Durably admit one session input and schedule agent-loop execution unless resume is false.",
  "summary": "Send message",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Message.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "text": {
              "type": "string"
            },
            "files": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/PromptInput.FileAttachment"
              }
            },
            "agents": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Prompt.AgentAttachment"
              }
            },
            "skills": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/PromptInput.SkillAttachment"
              }
            },
            "metadata": {
              "type": "object"
            },
            "delivery": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Inbox.Delivery"
                },
                {
                  "type": "null"
                }
              ]
            },
            "resume": {
              "anyOf": [
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "text"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/command

<a id="session.command"></a>

### POST /api/session/{sessionID}/command — session.command

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.command",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | CommandNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/CommandNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "500": {
      "description": "CommandExecutionError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/CommandExecutionErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Execute a slash command callback immediately.",
  "summary": "Run command",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "text": {
              "type": "string"
            },
            "files": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/PromptInput.FileAttachment"
              }
            },
            "agents": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Prompt.AgentAttachment"
              }
            },
            "skills": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/PromptInput.SkillAttachment"
              }
            },
            "delivery": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Inbox.Delivery"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "name",
            "text"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/session/{sessionID}/skill

<a id="experimental.session.skill"></a>

### POST /api/experimental/session/{sessionID}/skill — experimental.session.skill

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.skill",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | SkillNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/SkillNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Activate a skill for a session by appending a skill message and resuming execution.",
  "summary": "Activate skill",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/components/schemas/Skill.ID"
            },
            "resume": {
              "anyOf": [
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "id"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/synthetic

<a id="session.synthetic"></a>

### POST /api/session/{sessionID}/synthetic — session.synthetic

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.synthetic",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Inbox.Synthetic"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Durably admit synthetic session input and schedule execution unless resume is false.",
  "summary": "Add synthetic message",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Message.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "text": {
              "type": "string"
            },
            "description": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            },
            "metadata": {
              "type": "object"
            },
            "delivery": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Inbox.Delivery"
                },
                {
                  "type": "null"
                }
              ]
            },
            "resume": {
              "anyOf": [
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "text"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/shell

<a id="session.shell"></a>

### POST /api/session/{sessionID}/shell — session.shell

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.shell",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Execute one shell command in the session's working directory. Emits a shell.started event before execution and a shell.ended event with the merged output after.",
  "summary": "Run shell command",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Message.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "command": {
              "type": "string"
            }
          },
          "required": [
            "command"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/compact

<a id="session.compact"></a>

### POST /api/session/{sessionID}/compact — session.compact

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.compact",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Inbox.Compaction"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Durably admit a session compaction request. Steers by default: it runs at the next step boundary instead of waiting behind queued prompts.",
  "summary": "Compact session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Message.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "delivery": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Session.Inbox.Delivery"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/session/{sessionID}/wait

<a id="experimental.session.wait"></a>

### POST /api/experimental/session/{sessionID}/wait — experimental.session.wait

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.wait",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Wait for a session agent loop to become idle.",
  "summary": "Wait for session"
}
```

## /api/session/{sessionID}/revert/stage

<a id="session.revert.stage"></a>

### POST /api/session/{sessionID}/revert/stage — session.revert.stage

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.revert.stage",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Revert"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "MessageNotFoundError | SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MessageNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "SessionBusyError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionBusyErrorEncoded"
          }
        }
      }
    },
    "500": {
      "description": "UnknownError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnknownErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Stage or move a reversible session boundary and optionally apply its file changes.",
  "summary": "Stage session revert",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "messageID": {
              "$ref": "#/components/schemas/Session.Message.ID"
            },
            "files": {
              "anyOf": [
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "messageID"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/revert

<a id="session.revert.clear"></a>

### DELETE /api/session/{sessionID}/revert — session.revert.clear

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.revert.clear",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "SessionBusyError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionBusyErrorEncoded"
          }
        }
      }
    },
    "500": {
      "description": "UnknownError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnknownErrorEncoded"
          }
        }
      }
    }
  },
  "summary": "Clear staged revert"
}
```

## /api/session/{sessionID}/revert/commit

<a id="session.revert.commit"></a>

### POST /api/session/{sessionID}/revert/commit — session.revert.commit

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.revert.commit",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "SessionBusyError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionBusyErrorEncoded"
          }
        }
      }
    }
  },
  "summary": "Commit staged revert"
}
```

## /api/session/{sessionID}/context

<a id="session.context"></a>

### GET /api/session/{sessionID}/context — session.context

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.context",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Session.Message.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    },
    "500": {
      "description": "UnknownError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnknownErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve the active context messages for a session (all messages after the last compaction).",
  "summary": "Get session context"
}
```

## /api/session/{sessionID}/diff

<a id="session.diff"></a>

### GET /api/session/{sessionID}/diff — session.diff

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.diff",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "from",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Session.Message.ID"
          },
          {
            "type": "null"
          }
        ],
        "description": "User message whose turn to diff. Defaults to the turn of the newest user message."
      },
      "required": false
    },
    {
      "name": "to",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Session.Message.ID"
          },
          {
            "type": "null"
          }
        ],
        "description": "Later user message whose turn ends the range. Defaults to the turn of `from` alone."
      },
      "required": false
    },
    {
      "name": "context",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Unchanged lines around each hunk. Omit for full-file patches."
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/FileDiff.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "MessageNotFoundError | SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/MessageNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "500": {
      "description": "UnknownError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnknownErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Structured per-file diffs of the files a turn changed. A turn runs from the first prompt after the session was last idle until its next idle marker, so prompts steered in while it was busy belong to the same turn; `to` extends the range through a later turn. Compares the range's first recorded snapshot with its last; a step still running in the active session compares against the working copy. Ranges that span a location change are rejected. In sessions without any idle marker, a prompt's turn spans until the next user message.",
  "summary": "Diff session turns"
}
```

## /api/session/{sessionID}/inbox

<a id="session.inbox.list"></a>

### GET /api/session/{sessionID}/inbox — session.inbox.list

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.inbox.list",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Session.Inbox.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List durable enqueued session work not yet delivered, ordered by enqueue sequence. Includes user, synthetic, compaction, and move items.",
  "summary": "List session inbox"
}
```

## /api/session/{sessionID}/inbox/{inboxID}

<a id="session.inbox.cancel"></a>

### DELETE /api/session/{sessionID}/inbox/{inboxID} — session.inbox.cancel

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.inbox.cancel",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "inboxID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.Message.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Cancel an inbox item that has not yet been delivered. Unavailable items are a no-op.",
  "summary": "Cancel inbox input"
}
```

<a id="session.inbox.update"></a>

### PATCH /api/session/{sessionID}/inbox/{inboxID} — session.inbox.update

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.inbox.update",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "inboxID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.Message.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Change a pending inbox item's delivery mode. Steering wakes session execution.",
  "summary": "Update inbox item",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "delivery": {
              "$ref": "#/components/schemas/Session.Inbox.Delivery"
            }
          },
          "required": [
            "delivery"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/session/{sessionID}/instructions/entries

<a id="experimental.session.instructions.entry.list"></a>

### GET /api/experimental/session/{sessionID}/instructions/entries — experimental.session.instructions.entry.list

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.instructions.entry.list",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/InstructionEntry.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "List API-managed instruction entries attached to the session.",
  "summary": "List instruction entries"
}
```

## /api/experimental/session/{sessionID}/instructions/entries/{key}

<a id="experimental.session.instructions.entry.put"></a>

### PUT /api/experimental/session/{sessionID}/instructions/entries/{key} — experimental.session.instructions.entry.put

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.instructions.entry.put",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "key",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/InstructionEntry.Key"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "413": {
      "description": "InstructionEntryValueTooLargeError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InstructionEntryValueTooLargeErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Attach or replace one durable instruction entry. Changes announce as updates at the next step boundary.",
  "summary": "Put instruction entry",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "value": {}
          },
          "required": [
            "value"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

<a id="experimental.session.instructions.entry.remove"></a>

### DELETE /api/experimental/session/{sessionID}/instructions/entries/{key} — experimental.session.instructions.entry.remove

```json
{
  "tags": [
    "session"
  ],
  "operationId": "experimental.session.instructions.entry.remove",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "key",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/InstructionEntry.Key"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Remove one instruction entry; the removal is announced to the model at the next step boundary.",
  "summary": "Remove instruction entry"
}
```

## /api/session/{sessionID}/generate

<a id="session.generate"></a>

### POST /api/session/{sessionID}/generate — session.generate

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.generate",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "SessionGenerateResponse",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionGenerateResponse"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Generate transient text from the current session context without mutating session history.",
  "summary": "Generate text from session context",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string"
            }
          },
          "required": [
            "prompt"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/session/{sessionID}/log

<a id="session.log"></a>

### GET /api/experimental/session/{sessionID}/log — session.log

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.log",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "after",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Event.SeqEncoded"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "follow",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "true",
              "false"
            ]
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "text/event-stream": {
          "schema": {
            "type": "object",
            "properties": {
              "id": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "event": {
                "type": "string"
              },
              "data": {
                "$ref": "#/components/schemas/SessionLogItemEncoded"
              }
            },
            "required": [
              "event",
              "data"
            ],
            "additionalProperties": false
          },
          "x-effect-stream": {
            "encoding": "sse",
            "causeSchema": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "_tag": {
                        "type": "string",
                        "enum": [
                          "Fail"
                        ]
                      },
                      "error": {
                        "not": {}
                      }
                    },
                    "required": [
                      "_tag",
                      "error"
                    ],
                    "additionalProperties": false
                  },
                  {
                    "type": "object",
                    "properties": {
                      "_tag": {
                        "type": "string",
                        "enum": [
                          "Die"
                        ]
                      },
                      "defect": {}
                    },
                    "required": [
                      "_tag",
                      "defect"
                    ],
                    "additionalProperties": false
                  },
                  {
                    "type": "object",
                    "properties": {
                      "_tag": {
                        "type": "string",
                        "enum": [
                          "Interrupt"
                        ]
                      },
                      "fiberId": {
                        "anyOf": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "null"
                          }
                        ]
                      }
                    },
                    "required": [
                      "_tag",
                      "fiberId"
                    ],
                    "additionalProperties": false
                  }
                ]
              }
            },
            "errorSchema": {
              "not": {}
            },
            "failureEvent": "effect/http-api/stream/failure"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Experimental durable session event log. Reads events after an exclusive aggregate sequence and continues with live events when follow=true.",
  "summary": "Read the session log"
}
```

## /api/session/{sessionID}/interrupt

<a id="session.interrupt"></a>

### POST /api/session/{sessionID}/interrupt — session.interrupt

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.interrupt",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "resume",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "true",
              "false"
            ]
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "SessionInterruptResponse",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionInterruptResponse"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Interrupt active execution owned by this OpenCode process. Returns interrupted=true when an active execution was interrupted and false for the idle no-op. When resume=true, execution resumes pending steering input and next-in-line control items (manual compaction, moves) while queued prompts remain parked.",
  "summary": "Interrupt session execution"
}
```

## /api/session/{sessionID}/background

<a id="session.background"></a>

### POST /api/session/{sessionID}/background — session.background

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.background",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Move active foreground backgroundable tools for this session into background observation. Idle requests are a no-op.",
  "summary": "Background blocking session tools"
}
```

## /api/session/{sessionID}/message/{messageID}

<a id="session.message.get"></a>

### GET /api/session/{sessionID}/message/{messageID} — session.message.get

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.message.get",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "messageID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.Message.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Session.Message.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | MessageNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/MessageNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve one projected message owned by the Session.",
  "summary": "Get session message"
}
```

## /api/session/{sessionID}/form

<a id="session.form.list"></a>

### GET /api/session/{sessionID}/form — session.form.list

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.form.list",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Form.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve pending forms for a session.",
  "summary": "List session forms"
}
```

<a id="session.form.create"></a>

### POST /api/session/{sessionID}/form — session.form.create

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.form.create",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Form.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Create a form for a session.",
  "summary": "Create session form",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Form.CreatePayload"
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/form/{formID}

<a id="session.form.get"></a>

### GET /api/session/{sessionID}/form/{formID} — session.form.get

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.form.get",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "formID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Form.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Form.Detail"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | FormNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/FormNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve a form and its current state for a session.",
  "summary": "Get session form"
}
```

<a id="session.form.cancel"></a>

### DELETE /api/session/{sessionID}/form/{formID} — session.form.cancel

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.form.cancel",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "formID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Form.ID"
      },
      "required": true
    },
    {
      "name": "message",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | FormNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/FormNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "FormAlreadySettledError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/FormAlreadySettledErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Cancel a pending form, optionally telling the asker why it was not answered.",
  "summary": "Cancel form"
}
```

## /api/session/{sessionID}/form/{formID}/reply

<a id="session.form.reply"></a>

### POST /api/session/{sessionID}/form/{formID}/reply — session.form.reply

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.form.reply",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "formID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Form.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "FormInvalidAnswerError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/FormInvalidAnswerErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | FormNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/FormNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "409": {
      "description": "FormAlreadySettledError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/FormAlreadySettledErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Submit an answer to a pending form.",
  "summary": "Reply to form",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Form.Reply"
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/environment

<a id="session.environment"></a>

### PUT /api/session/{sessionID}/environment — session.environment

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.environment",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Replace the process environment used by local shell commands for this session.",
  "summary": "Set session environment",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "variables": {
              "type": "object",
              "additionalProperties": {
                "type": "string"
              }
            }
          },
          "required": [
            "variables"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/view

<a id="session.view"></a>

### POST /api/session/{sessionID}/view — session.view

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.view",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Mark the idle transition observed by the viewer as viewed.",
  "summary": "View session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "idle": {
              "type": "number"
            }
          },
          "required": [
            "idle"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/session/{sessionID}/message

<a id="session.message.list"></a>

### GET /api/session/{sessionID}/message — session.message.list

```json
{
  "tags": [
    "session"
  ],
  "operationId": "session.message.list",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "limit",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "Maximum number of messages to return. When omitted, the endpoint returns its default page size."
      },
      "required": false
    },
    {
      "name": "order",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "asc",
              "desc"
            ]
          },
          {
            "type": "null"
          }
        ],
        "description": "Message order for the first page. Use desc for newest first or asc for oldest first."
      },
      "required": false
    },
    {
      "name": "cursor",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "description": "Opaque pagination cursor returned as cursor.previous or cursor.next in the previous response. Do not combine with order."
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "type",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "agent-switched",
              "model-switched",
              "location-switched",
              "user",
              "synthetic",
              "system",
              "skill",
              "shell",
              "assistant",
              "compaction"
            ]
          },
          {
            "type": "null"
          }
        ],
        "description": "Filter by message type before pagination. When omitted, all message types are returned. Pass the same type when following cursors."
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "SessionMessagesResponse",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionMessagesResponse"
          }
        }
      }
    },
    "400": {
      "description": "InvalidCursorError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/InvalidCursorErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
          }
        }
      }
    },
    "500": {
      "description": "UnknownError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnknownErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve projected messages for a session, optionally filtered by type. Items keep the requested order across pages; use cursor.next or cursor.previous to move through the ordered timeline, passing the same type filter on each page.",
  "summary": "Get session messages"
}
```

## /api/model

<a id="model.list"></a>

### GET /api/model — model.list

```json
{
  "tags": [
    "model"
  ],
  "operationId": "model.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Model.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve the current snapshot of available models ordered by release date. The snapshot may precede initial plugin settlement.",
  "summary": "List models"
}
```

## /api/model/default

<a id="model.default"></a>

### GET /api/model/default — model.default

```json
{
  "tags": [
    "model"
  ],
  "operationId": "model.default",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/Model.Info"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve the model used when a session has no explicit model selection.",
  "summary": "Get default model"
}
```

## /api/experimental/generate

<a id="experimental.generate.text"></a>

### POST /api/experimental/generate — experimental.generate.text

```json
{
  "tags": [
    "generate"
  ],
  "operationId": "experimental.generate.text",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "GenerateTextResponse",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/GenerateTextResponse"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Run one stateless model generation using the server's base configuration and return the assistant text. Uses the base configuration's default model when none is specified.",
  "summary": "Generate text",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "prompt": {
              "type": "string"
            },
            "model": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Model.Ref"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "prompt"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/provider

<a id="provider.list"></a>

### GET /api/provider — provider.list

```json
{
  "tags": [
    "provider"
  ],
  "operationId": "provider.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Provider.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve active AI providers so clients can show provider availability and configuration.",
  "summary": "List providers"
}
```

## /api/provider/{providerID}

<a id="provider.get"></a>

### GET /api/provider/{providerID} — provider.get

```json
{
  "tags": [
    "provider"
  ],
  "operationId": "provider.get",
  "parameters": [
    {
      "name": "providerID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Provider.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Provider.Info"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ProviderNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ProviderNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve a single AI provider so clients can inspect its availability and endpoint settings.",
  "summary": "Get provider"
}
```

## /api/integration

<a id="integration.list"></a>

### GET /api/integration — integration.list

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Integration.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve available integrations and their authentication methods.",
  "summary": "List integrations"
}
```

## /api/integration/{integrationID}

<a id="integration.get"></a>

### GET /api/integration/{integrationID} — integration.get

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.get",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Integration.Info"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve one integration and its authentication methods.",
  "summary": "Get integration"
}
```

## /api/experimental/integration/wellknown

<a id="experimental.integration.wellknown.add"></a>

### POST /api/experimental/integration/wellknown — experimental.integration.wellknown.add

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "experimental.integration.wellknown.add",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Discover and persist an experimental wellknown integration source.",
  "summary": "Add wellknown integration",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "url": {
              "type": "string"
            }
          },
          "required": [
            "url"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/integration/{integrationID}/connect/key

<a id="integration.connect.key"></a>

### POST /api/integration/{integrationID}/connect/key — integration.connect.key

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.connect.key",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Run a key authentication method and store the resulting credential.",
  "summary": "Connect with key",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "key": {
              "type": "string"
            },
            "answer": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Form.Answer"
                },
                {
                  "type": "null"
                }
              ]
            },
            "label": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "key"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/integration/{integrationID}/connect/external

<a id="integration.connect.external"></a>

### POST /api/integration/{integrationID}/connect/external — integration.connect.external

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.connect.external",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Run an external authentication method and store a reference to its credential source.",
  "summary": "Connect with external credentials",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "methodID": {
              "$ref": "#/components/schemas/Integration.MethodID"
            },
            "answer": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Form.Answer"
                },
                {
                  "type": "null"
                }
              ]
            },
            "label": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "methodID"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/integration/{integrationID}/connect/oauth

<a id="integration.oauth.connect"></a>

### POST /api/integration/{integrationID}/connect/oauth — integration.oauth.connect

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.oauth.connect",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Integration.AttemptEncoded"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Start an OAuth attempt and return the authorization details.",
  "summary": "Begin OAuth connection",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "methodID": {
              "$ref": "#/components/schemas/Integration.MethodID"
            },
            "answer": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Form.Answer"
                },
                {
                  "type": "null"
                }
              ]
            },
            "label": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "methodID"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/integration/{integrationID}/connect/oauth/{attemptID}

<a id="integration.oauth.status"></a>

### GET /api/integration/{integrationID}/connect/oauth/{attemptID} — integration.oauth.status

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.oauth.status",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "attemptID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.AttemptID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Integration.AttemptStatus"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | IntegrationAttemptNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/IntegrationAttemptNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Poll the current status of an OAuth attempt.",
  "summary": "Get OAuth attempt status"
}
```

<a id="integration.oauth.cancel"></a>

### DELETE /api/integration/{integrationID}/connect/oauth/{attemptID} — integration.oauth.cancel

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.oauth.cancel",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "attemptID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.AttemptID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Cancel an OAuth attempt and release its resources.",
  "summary": "Cancel OAuth connection"
}
```

## /api/integration/{integrationID}/connect/oauth/{attemptID}/complete

<a id="integration.oauth.complete"></a>

### POST /api/integration/{integrationID}/connect/oauth/{attemptID}/complete — integration.oauth.complete

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.oauth.complete",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "attemptID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.AttemptID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | IntegrationAttemptNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/IntegrationAttemptNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Complete a code-based OAuth attempt and store the resulting credential.",
  "summary": "Complete OAuth connection",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "code": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/integration/{integrationID}/connect/command

<a id="integration.command.connect"></a>

### POST /api/integration/{integrationID}/connect/command — integration.command.connect

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.command.connect",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Integration.CommandAttempt"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | IntegrationMethodNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/IntegrationMethodNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Start a command authentication attempt.",
  "summary": "Begin command connection",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "methodID": {
              "$ref": "#/components/schemas/Integration.MethodID"
            },
            "label": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "methodID"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/integration/{integrationID}/connect/command/{attemptID}

<a id="integration.command.status"></a>

### GET /api/integration/{integrationID}/connect/command/{attemptID} — integration.command.status

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.command.status",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "attemptID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.AttemptID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Integration.CommandAttemptStatus"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "IntegrationNotFoundError | IntegrationAttemptNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/IntegrationNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/IntegrationAttemptNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Poll the current status and output of a command authentication attempt.",
  "summary": "Get command attempt status"
}
```

<a id="integration.command.cancel"></a>

### DELETE /api/integration/{integrationID}/connect/command/{attemptID} — integration.command.cancel

```json
{
  "tags": [
    "integration"
  ],
  "operationId": "integration.command.cancel",
  "parameters": [
    {
      "name": "integrationID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.ID"
      },
      "required": true
    },
    {
      "name": "attemptID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Integration.AttemptID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Cancel a command authentication attempt and terminate its process.",
  "summary": "Cancel command connection"
}
```

## /api/mcp

<a id="mcp.list"></a>

### GET /api/mcp — mcp.list

```json
{
  "tags": [
    "mcp"
  ],
  "operationId": "mcp.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Mcp.Server"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve configured MCP servers and their connection status.",
  "summary": "List MCP servers"
}
```

## /api/experimental/mcp/{server}

<a id="experimental.mcp.add"></a>

### PUT /api/experimental/mcp/{server} — experimental.mcp.add

```json
{
  "tags": [
    "mcp"
  ],
  "operationId": "experimental.mcp.add",
  "parameters": [
    {
      "name": "server",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Add an MCP server at runtime or replace an existing one, connecting it immediately.",
  "summary": "Add MCP server",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "config": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Mcp.LocalConfigEncoded"
                },
                {
                  "$ref": "#/components/schemas/Mcp.RemoteConfigEncoded"
                }
              ]
            }
          },
          "required": [
            "config"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

<a id="experimental.mcp.remove"></a>

### DELETE /api/experimental/mcp/{server} — experimental.mcp.remove

```json
{
  "tags": [
    "mcp"
  ],
  "operationId": "experimental.mcp.remove",
  "parameters": [
    {
      "name": "server",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "McpServerNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/McpServerNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Stop an MCP server and remove it from the runtime set until restart.",
  "summary": "Remove MCP server"
}
```

## /api/experimental/mcp/{server}/connect

<a id="experimental.mcp.connect"></a>

### POST /api/experimental/mcp/{server}/connect — experimental.mcp.connect

```json
{
  "tags": [
    "mcp"
  ],
  "operationId": "experimental.mcp.connect",
  "parameters": [
    {
      "name": "server",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "McpServerNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/McpServerNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Connect an MCP server at runtime, overriding a disabled configuration until restart.",
  "summary": "Connect MCP server"
}
```

## /api/experimental/mcp/{server}/disconnect

<a id="experimental.mcp.disconnect"></a>

### POST /api/experimental/mcp/{server}/disconnect — experimental.mcp.disconnect

```json
{
  "tags": [
    "mcp"
  ],
  "operationId": "experimental.mcp.disconnect",
  "parameters": [
    {
      "name": "server",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "McpServerNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/McpServerNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Disconnect an MCP server at runtime, removing its tools until reconnected.",
  "summary": "Disconnect MCP server"
}
```

## /api/mcp/resource

<a id="mcp.resource.catalog"></a>

### GET /api/mcp/resource — mcp.resource.catalog

```json
{
  "tags": [
    "mcp"
  ],
  "operationId": "mcp.resource.catalog",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Mcp.ResourceCatalog"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve resources and resource templates from connected MCP servers.",
  "summary": "List MCP resources"
}
```

## /api/credential

<a id="credential.list"></a>

### GET /api/credential — credential.list

```json
{
  "tags": [
    "credential"
  ],
  "operationId": "credential.list",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Credential.Entry"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List every stored integration credential, including its secret value.",
  "summary": "List credentials"
}
```

<a id="credential.create"></a>

### POST /api/credential — credential.create

```json
{
  "tags": [
    "credential"
  ],
  "operationId": "credential.create",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Credential.Entry"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Store an integration credential. It becomes the integration's active credential unless activate is false and the integration already has one. Fails with a conflict when the requested ID already exists.",
  "summary": "Create credential",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Credential.CreateInput"
        }
      }
    },
    "required": true
  }
}
```

## /api/credential/{credentialID}

<a id="credential.update"></a>

### PATCH /api/credential/{credentialID} — credential.update

```json
{
  "tags": [
    "credential"
  ],
  "operationId": "credential.update",
  "parameters": [
    {
      "name": "credentialID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Credential.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Update a stored credential label.",
  "summary": "Update credential",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string"
            }
          },
          "required": [
            "label"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

<a id="credential.remove"></a>

### DELETE /api/credential/{credentialID} — credential.remove

```json
{
  "tags": [
    "credential"
  ],
  "operationId": "credential.remove",
  "parameters": [
    {
      "name": "credentialID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Credential.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Remove a stored integration credential.",
  "summary": "Remove credential"
}
```

## /api/credential/{credentialID}/activate

<a id="credential.activate"></a>

### POST /api/credential/{credentialID}/activate — credential.activate

```json
{
  "tags": [
    "credential"
  ],
  "operationId": "credential.activate",
  "parameters": [
    {
      "name": "credentialID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Credential.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Activate a stored integration credential.",
  "summary": "Activate credential"
}
```

## /api/project

<a id="project.list"></a>

### GET /api/project — project.list

```json
{
  "tags": [
    "project"
  ],
  "operationId": "project.list",
  "parameters": [
    {
      "name": "archived",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string",
            "enum": [
              "true",
              "false"
            ]
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Project"
            }
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List known projects. Archived projects are excluded unless archived=true.",
  "summary": "List projects"
}
```

## /api/project/{projectID}

<a id="project.update"></a>

### PATCH /api/project/{projectID} — project.update

```json
{
  "tags": [
    "project"
  ],
  "operationId": "project.update",
  "parameters": [
    {
      "name": "projectID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Project.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Project",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/Project"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ProjectNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ProjectNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Update the project canonical directory, display metadata, and workspace commands.",
  "summary": "Update project",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "canonical": {
              "$ref": "#/components/schemas/AbsolutePath"
            },
            "name": {
              "type": "string"
            },
            "icon": {
              "$ref": "#/components/schemas/Project.Icon"
            },
            "commands": {
              "$ref": "#/components/schemas/Project.Commands"
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/form

<a id="form.list"></a>

### GET /api/form — form.list

```json
{
  "tags": [
    "form"
  ],
  "operationId": "form.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Form.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve pending forms for a location.",
  "summary": "List pending forms"
}
```

## /api/permission/request

<a id="permission.request.list"></a>

### GET /api/permission/request — permission.request.list

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "permission.request.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Permission.Request"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve pending permission requests for a location.",
  "summary": "List pending permission requests"
}
```

## /api/permission/saved

<a id="permission.saved.list"></a>

### GET /api/permission/saved — permission.saved.list

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "permission.saved.list",
  "parameters": [
    {
      "name": "projectID",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Project.ID"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/PermissionSaved.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve saved permissions, optionally filtered by project.",
  "summary": "List saved permissions"
}
```

## /api/permission/saved/{id}

<a id="permission.saved.remove"></a>

### DELETE /api/permission/saved/{id} — permission.saved.remove

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "permission.saved.remove",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/PermissionSaved.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Remove a saved permission by ID.",
  "summary": "Remove saved permission"
}
```

## /api/session/{sessionID}/permission

<a id="session.permission.create"></a>

### POST /api/session/{sessionID}/permission — session.permission.create

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "session.permission.create",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "object",
                "properties": {
                  "id": {
                    "$ref": "#/components/schemas/Permission.ID"
                  },
                  "effect": {
                    "$ref": "#/components/schemas/Permission.Effect"
                  }
                },
                "required": [
                  "id",
                  "effect"
                ],
                "additionalProperties": false
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Evaluate and, when approval is required, create a permission request for a session.",
  "summary": "Create permission request",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "id": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Permission.ID"
                },
                {
                  "type": "null"
                }
              ]
            },
            "action": {
              "type": "string"
            },
            "resources": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "save": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "metadata": {
              "type": "object"
            },
            "source": {
              "$ref": "#/components/schemas/Permission.Source"
            },
            "agent": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/Agent.ID"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "action",
            "resources"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

<a id="session.permission.list"></a>

### GET /api/session/{sessionID}/permission — session.permission.list

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "session.permission.list",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Permission.Request"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve pending permission requests owned by a session.",
  "summary": "List session permission requests"
}
```

## /api/session/{sessionID}/permission/{requestID}

<a id="session.permission.get"></a>

### GET /api/session/{sessionID}/permission/{requestID} — session.permission.get

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "session.permission.get",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "requestID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Permission.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/Permission.Request"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | PermissionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/PermissionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Retrieve a pending permission request owned by a session.",
  "summary": "Get permission request"
}
```

## /api/session/{sessionID}/permission/{requestID}/reply

<a id="session.permission.reply"></a>

### POST /api/session/{sessionID}/permission/{requestID}/reply — session.permission.reply

```json
{
  "tags": [
    "permission"
  ],
  "operationId": "session.permission.reply",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "requestID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Permission.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "SessionNotFoundError | PermissionNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/SessionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/PermissionNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Respond to a pending permission request owned by a session.",
  "summary": "Reply to pending permission request",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "decision": {
              "$ref": "#/components/schemas/Permission.Reply"
            },
            "message": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "required": [
            "decision"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/fs/read/*

<a id="fs.read"></a>

### GET /api/fs/read/* — fs.read

```json
{
  "tags": [
    "filesystem"
  ],
  "operationId": "fs.read",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/octet-stream": {
          "schema": {
            "type": "string",
            "format": "binary"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "FileNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/FileNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Stream one file relative to the requested location with ETag, Last-Modified, and single-range HTTP Range support (206 Partial Content, 416 Range Not Satisfiable, and 304 Not Modified; multi-range and malformed Range headers fall back to 200).",
  "summary": "Read file"
}
```

## /api/fs/list

<a id="fs.list"></a>

### GET /api/fs/list — fs.list

```json
{
  "tags": [
    "filesystem"
  ],
  "operationId": "fs.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "path",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ],
        "description": "An absolute path or a path relative to the requested location. Defaults to the location directory."
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/FileSystem.Entry"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "FileNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/FileNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "List direct children using an absolute path or a path relative to the requested location, including parents and siblings outside its directory. Entry paths remain relative to the requested location; listing does not switch locations.",
  "summary": "List directory"
}
```

## /api/fs/find

<a id="fs.find"></a>

### GET /api/fs/find — fs.find

```json
{
  "tags": [
    "filesystem"
  ],
  "operationId": "fs.find",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "query",
      "in": "query",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "type",
      "in": "query",
      "schema": {
        "type": "string",
        "enum": [
          "file",
          "directory"
        ]
      },
      "required": false
    },
    {
      "name": "limit",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/FileSystem.Entry"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Find recursively ranked filesystem entries relative to the requested location.",
  "summary": "Find files"
}
```

## /api/experimental/fs/write

<a id="experimental.fs.write"></a>

### POST /api/experimental/fs/write — experimental.fs.write

```json
{
  "tags": [
    "filesystem"
  ],
  "operationId": "experimental.fs.write",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "path",
      "in": "query",
      "schema": {
        "type": "string",
        "description": "An absolute path or a path relative to the requested location. Missing parent directories are created."
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/FileSystem.Write"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Write the raw request body to an absolute path or a path relative to the requested location, creating parent directories, and return the resolved absolute path. Unlike read, the target is not confined to the location. Experimental: may change without compatibility guarantees.",
  "summary": "Write file",
  "requestBody": {
    "content": {
      "application/octet-stream": {
        "schema": {
          "type": "string",
          "format": "binary"
        }
      }
    },
    "required": true
  }
}
```

## /api/command

<a id="command.list"></a>

### GET /api/command — command.list

```json
{
  "tags": [
    "command"
  ],
  "operationId": "command.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Command.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve currently registered commands.",
  "summary": "List commands"
}
```

## /api/skill

<a id="skill.list"></a>

### GET /api/skill — skill.list

```json
{
  "tags": [
    "skill"
  ],
  "operationId": "skill.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Skill.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Retrieve currently registered skills.",
  "summary": "List skills"
}
```

## /api/rpc/{rpcID}/{method}

<a id="rpc.call"></a>

### POST /api/rpc/{rpcID}/{method} — rpc.call

```json
{
  "tags": [
    "rpc"
  ],
  "operationId": "rpc.call",
  "parameters": [
    {
      "name": "rpcID",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "method",
      "in": "path",
      "schema": {
        "type": "string"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Rpc.Output",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/Rpc.Output"
          }
        }
      }
    },
    "400": {
      "description": "RpcError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/RpcErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "500": {
      "description": "RpcInternalError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/RpcInternalErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Dispatch a method to the currently registered RPC at the requested location.",
  "summary": "Call a plugin RPC",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Rpc.Input"
        }
      }
    },
    "required": true
  }
}
```

## /api/event

<a id="event.subscribe"></a>

### GET /api/event — event.subscribe

```json
{
  "tags": [
    "event"
  ],
  "operationId": "event.subscribe",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "text/event-stream": {
          "schema": {
            "type": "object",
            "properties": {
              "id": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "event": {
                "type": "string"
              },
              "data": {
                "$ref": "#/components/schemas/V2EventEncoded"
              }
            },
            "required": [
              "event",
              "data"
            ],
            "additionalProperties": false
          },
          "x-effect-stream": {
            "encoding": "sse",
            "causeSchema": {
              "type": "array",
              "items": {
                "anyOf": [
                  {
                    "type": "object",
                    "properties": {
                      "_tag": {
                        "type": "string",
                        "enum": [
                          "Fail"
                        ]
                      },
                      "error": {
                        "not": {}
                      }
                    },
                    "required": [
                      "_tag",
                      "error"
                    ],
                    "additionalProperties": false
                  },
                  {
                    "type": "object",
                    "properties": {
                      "_tag": {
                        "type": "string",
                        "enum": [
                          "Die"
                        ]
                      },
                      "defect": {}
                    },
                    "required": [
                      "_tag",
                      "defect"
                    ],
                    "additionalProperties": false
                  },
                  {
                    "type": "object",
                    "properties": {
                      "_tag": {
                        "type": "string",
                        "enum": [
                          "Interrupt"
                        ]
                      },
                      "fiberId": {
                        "anyOf": [
                          {
                            "type": "number"
                          },
                          {
                            "type": "null"
                          }
                        ]
                      }
                    },
                    "required": [
                      "_tag",
                      "fiberId"
                    ],
                    "additionalProperties": false
                  }
                ]
              }
            },
            "errorSchema": {
              "not": {}
            },
            "failureEvent": "effect/http-api/stream/failure"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Subscribe to native events and plugin RPC events across all server locations. Volatile by contract: a slow consumer overflows and fails the stream, and events during disconnection are missed.",
  "summary": "Subscribe to events"
}
```

## /api/pty

<a id="pty.list"></a>

### GET /api/pty — pty.list

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Pty"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List PTY sessions for a location, including exited sessions retained until removal.",
  "summary": "List PTY sessions"
}
```

<a id="pty.create"></a>

### POST /api/pty — pty.create

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.create",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Pty"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Create a pseudo-terminal session for a location.",
  "summary": "Create PTY session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "command": {
              "type": "string"
            },
            "args": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "cwd": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "env": {
              "type": "object",
              "additionalProperties": {
                "type": "string"
              }
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/pty/{ptyID}

<a id="pty.get"></a>

### GET /api/pty/{ptyID} — pty.get

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.get",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Pty"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Get one PTY session, including its exit code once exited.",
  "summary": "Get PTY session"
}
```

<a id="pty.update"></a>

### PUT /api/pty/{ptyID} — pty.update

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.update",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Pty"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Update the title or viewport size of one PTY session.",
  "summary": "Update PTY session",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "size": {
              "type": "object",
              "properties": {
                "rows": {
                  "type": "integer",
                  "exclusiveMinimum": 0
                },
                "cols": {
                  "type": "integer",
                  "exclusiveMinimum": 0
                }
              },
              "required": [
                "rows",
                "cols"
              ],
              "additionalProperties": false
            }
          },
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

<a id="pty.remove"></a>

### DELETE /api/pty/{ptyID} — pty.remove

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.remove",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Terminate and remove one PTY session.",
  "summary": "Remove PTY session"
}
```

## /api/pty/{ptyID}/connect-token

<a id="pty.connect.token"></a>

### POST /api/pty/{ptyID}/connect-token — pty.connect.token

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.connect.token",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "name": "x-opencode-ticket",
      "in": "header",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/PtyTicket.ConnectToken"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "403": {
      "description": "ForbiddenError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ForbiddenErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Create a short-lived single-use ticket for opening a PTY WebSocket connection.",
  "summary": "Create PTY WebSocket token"
}
```

## /api/pty/{ptyID}/connect

<a id="pty.connect"></a>

### GET /api/pty/{ptyID}/connect — pty.connect

```json
{
  "tags": [
    "pty"
  ],
  "operationId": "pty.connect",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "in": "query",
      "name": "location[directory]",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "cursor",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "ticket",
      "schema": {
        "type": "string"
      }
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "boolean"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "403": {
      "description": "ForbiddenError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ForbiddenErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Establish a WebSocket connection streaming PTY output and accepting terminal input.",
  "summary": "Connect to PTY session",
  "x-websocket": true
}
```

## /api/experimental/session/{sessionID}/terminal/read

<a id="server.experimental.persistentPty.read"></a>

### GET /api/experimental/session/{sessionID}/terminal/read — server.experimental.persistentPty.read

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.read",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    },
    {
      "name": "lines",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/PersistentPty.ReadLinesEncoded"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/PersistentPty.ReadResult"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Read the last physical rows without changing selection or taking control. Omitted lines uses the live terminal height; larger counts include retained history. Blank rows are preserved. Screen dimensions and cursor remain relative to the live screen. Returns null when no current terminal exists. Selection is server-local and resets on restart. Experimental: may change without compatibility guarantees.",
  "summary": "Read the session's most recently controlled terminal"
}
```

## /api/experimental/session/{sessionID}/terminal

<a id="server.experimental.persistentPty.list"></a>

### GET /api/experimental/session/{sessionID}/terminal — server.experimental.persistentPty.list

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.list",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/PersistentPty.Info"
                }
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

<a id="server.experimental.persistentPty.create"></a>

### POST /api/experimental/session/{sessionID}/terminal — server.experimental.persistentPty.create

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.create",
  "parameters": [
    {
      "name": "sessionID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Session.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/PersistentPty.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/PersistentPty.CreateInput"
        }
      }
    },
    "required": true
  }
}
```

## /api/experimental/persistent-pty/shutdown

<a id="server.experimental.persistentPty.shutdown"></a>

### POST /api/experimental/persistent-pty/shutdown — server.experimental.persistentPty.shutdown

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.shutdown",
  "parameters": [],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

## /api/experimental/persistent-pty/handoff

<a id="server.experimental.persistentPty.handoff"></a>

### POST /api/experimental/persistent-pty/handoff — server.experimental.persistentPty.handoff

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.handoff",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "handoff": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/PersistentPty.Handoff"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "required": [
              "handoff"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

## /api/experimental/persistent-pty/{ptyID}

<a id="server.experimental.persistentPty.get"></a>

### GET /api/experimental/persistent-pty/{ptyID} — server.experimental.persistentPty.get

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.get",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/PersistentPty.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

<a id="server.experimental.persistentPty.update"></a>

### PUT /api/experimental/persistent-pty/{ptyID} — server.experimental.persistentPty.update

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.update",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/PersistentPty.Info"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/PersistentPty.UpdateInput"
        }
      }
    },
    "required": true
  }
}
```

<a id="server.experimental.persistentPty.remove"></a>

### DELETE /api/experimental/persistent-pty/{ptyID} — server.experimental.persistentPty.remove

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.remove",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

## /api/experimental/persistent-pty/{ptyID}/snapshot

<a id="server.experimental.persistentPty.snapshot"></a>

### GET /api/experimental/persistent-pty/{ptyID}/snapshot — server.experimental.persistentPty.snapshot

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.snapshot",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/PersistentPty.Snapshot"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

## /api/experimental/persistent-pty/{ptyID}/connect-token

<a id="server.experimental.persistentPty.connectToken"></a>

### POST /api/experimental/persistent-pty/{ptyID}/connect-token — server.experimental.persistentPty.connectToken

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "server.experimental.persistentPty.connectToken",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "name": "x-opencode-ticket",
      "in": "header",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "data": {
                "$ref": "#/components/schemas/PtyTicket.ConnectToken"
              }
            },
            "required": [
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "403": {
      "description": "ForbiddenError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ForbiddenErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  }
}
```

## /api/experimental/persistent-pty/{ptyID}/connect

<a id="persistentPty.connect"></a>

### GET /api/experimental/persistent-pty/{ptyID}/connect — persistentPty.connect

```json
{
  "tags": [
    "persistentPty"
  ],
  "operationId": "persistentPty.connect",
  "parameters": [
    {
      "name": "ptyID",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Pty.ID"
      },
      "required": true
    },
    {
      "in": "query",
      "name": "cursor",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "role",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "attachment_id",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "takeover",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "input_protocol",
      "schema": {
        "type": "string"
      }
    },
    {
      "in": "query",
      "name": "ticket",
      "schema": {
        "type": "string"
      }
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "boolean"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "403": {
      "description": "ForbiddenError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ForbiddenErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "PtyNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/PtyNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Stream persistent PTY output through the OpenCode server.",
  "summary": "Connect to a persistent PTY",
  "x-websocket": true
}
```

## /api/shell

<a id="shell.list"></a>

### GET /api/shell — shell.list

```json
{
  "tags": [
    "shell"
  ],
  "operationId": "shell.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Shell.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List currently running shell commands for a location. Exited commands are not included.",
  "summary": "List running shell commands"
}
```

<a id="shell.create"></a>

### POST /api/shell — shell.create

```json
{
  "tags": [
    "shell"
  ],
  "operationId": "shell.create",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Shell.Info"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Spawn one non-interactive shell command for a location. Combined stdout/stderr is captured to a file pageable via output.",
  "summary": "Run shell command",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "command": {
              "type": "string"
            },
            "cwd": {
              "type": "string"
            },
            "timeout": {
              "type": "integer",
              "minimum": 0
            },
            "metadata": {
              "type": "object"
            }
          },
          "required": [
            "command"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/shell/{id}

<a id="shell.get"></a>

### GET /api/shell/{id} — shell.get

```json
{
  "tags": [
    "shell"
  ],
  "operationId": "shell.get",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Shell.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Shell.Info"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ShellNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ShellNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Get one shell command, including its status and exit code once exited.",
  "summary": "Get shell command"
}
```

<a id="shell.remove"></a>

### DELETE /api/shell/{id} — shell.remove

```json
{
  "tags": [
    "shell"
  ],
  "operationId": "shell.remove",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Shell.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Terminate and remove one shell command and its retained output.",
  "summary": "Remove shell command"
}
```

## /api/shell/{id}/output

<a id="shell.output"></a>

### GET /api/shell/{id}/output — shell.output

```json
{
  "tags": [
    "shell"
  ],
  "operationId": "shell.output",
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "schema": {
        "$ref": "#/components/schemas/Shell.ID"
      },
      "required": true
    },
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "cursor",
      "in": "query",
      "schema": {
        "type": "string",
        "pattern": "^[+-]?\\d*\\.?\\d+(?:[Ee][+-]?\\d+)?$"
      },
      "required": false
    },
    {
      "name": "limit",
      "in": "query",
      "schema": {
        "type": "string",
        "pattern": "^[+-]?\\d*\\.?\\d+(?:[Ee][+-]?\\d+)?$"
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "object",
                "properties": {
                  "output": {
                    "type": "string"
                  },
                  "cursor": {
                    "type": "integer",
                    "minimum": 0
                  },
                  "size": {
                    "type": "integer",
                    "minimum": 0
                  },
                  "truncated": {
                    "type": "boolean"
                  }
                },
                "required": [
                  "output",
                  "cursor",
                  "size",
                  "truncated"
                ],
                "additionalProperties": false
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ShellNotFoundError | LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/ShellNotFoundErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
              }
            ]
          }
        }
      }
    }
  },
  "description": "Page through captured combined output by absolute byte cursor.",
  "summary": "Read shell output"
}
```

## /api/reference

<a id="reference.list"></a>

### GET /api/reference — reference.list

```json
{
  "tags": [
    "reference"
  ],
  "operationId": "reference.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Reference.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List references available in the requested location.",
  "summary": "List references"
}
```

## /api/worktree

<a id="worktree.list"></a>

### GET /api/worktree — worktree.list

```json
{
  "tags": [
    "worktree"
  ],
  "operationId": "worktree.list",
  "parameters": [
    {
      "name": "projectID",
      "in": "query",
      "schema": {
        "$ref": "#/components/schemas/Project.ID"
      },
      "required": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Worktree.List",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/Worktree.List"
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ProjectNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ProjectNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Return the project's saved worktree inventory without loading configuration or running discovery.",
  "summary": "List worktrees"
}
```

<a id="worktree.create"></a>

### POST /api/worktree — worktree.create

```json
{
  "tags": [
    "worktree"
  ],
  "operationId": "worktree.create",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Worktree.Info",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/Worktree.Info"
          }
        }
      }
    },
    "400": {
      "description": "WorktreeError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/WorktreeErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ProjectNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ProjectNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Load the project's canonical configuration, create a local worktree using its selected strategy, then run the project's setup script.",
  "summary": "Create worktree",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Worktree.CreateInput"
        }
      }
    },
    "required": true
  }
}
```

<a id="worktree.remove"></a>

### DELETE /api/worktree — worktree.remove

```json
{
  "tags": [
    "worktree"
  ],
  "operationId": "worktree.remove",
  "parameters": [],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "WorktreeError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/WorktreeErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ProjectNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ProjectNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Load the project's canonical configuration and remove a saved worktree using its recorded strategy.",
  "summary": "Remove worktree",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Worktree.RemoveInput"
        }
      }
    },
    "required": true
  }
}
```

## /api/worktree/refresh

<a id="worktree.refresh"></a>

### POST /api/worktree/refresh — worktree.refresh

```json
{
  "tags": [
    "worktree"
  ],
  "operationId": "worktree.refresh",
  "parameters": [],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "WorktreeError | InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/WorktreeErrorEncoded"
              },
              {
                "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
              }
            ]
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "ProjectNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ProjectNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Load the project's canonical configuration, discover worktrees across known checkout roots using all available strategies, and reconcile saved state.",
  "summary": "Refresh worktrees",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "projectID": {
              "$ref": "#/components/schemas/Project.ID"
            }
          },
          "required": [
            "projectID"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/vcs/init

<a id="vcs.init"></a>

### POST /api/vcs/init — vcs.init

```json
{
  "tags": [
    "vcs"
  ],
  "operationId": "vcs.init",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "provider",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "409": {
      "description": "ConflictError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ConflictErrorEncoded"
          }
        }
      }
    },
    "501": {
      "description": "VcsInitNotSupportedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/VcsInitNotSupportedErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Initialize a repository using the selected VCS provider in a markerless project's directory and refresh its location services. Omitting provider defaults to git; built-in git and hg providers support initialization. An unknown provider returns 400; a registered provider without init returns 501.",
  "summary": "Initialize VCS repository"
}
```

## /api/vcs

<a id="vcs.get"></a>

### GET /api/vcs — vcs.get

```json
{
  "tags": [
    "vcs"
  ],
  "operationId": "vcs.get",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Vcs.Info"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Get current and default branch information for the requested location.",
  "summary": "VCS info"
}
```

## /api/vcs/base

<a id="vcs.base"></a>

### GET /api/vcs/base — vcs.base

```json
{
  "tags": [
    "vcs"
  ],
  "operationId": "vcs.base",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/Vcs.Base"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Infer a local review base from named branch creation history, or the repository default only when currently on that branch. Returns null before the first commit or when the provider lacks base metadata; ambiguous Git history requires an explicit base on diff requests.",
  "summary": "VCS review base"
}
```

## /api/vcs/status

<a id="vcs.status"></a>

### GET /api/vcs/status — vcs.status

```json
{
  "tags": [
    "vcs"
  ],
  "operationId": "vcs.status",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/Vcs.FileStatus"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List uncommitted working-copy changes relative to the requested location.",
  "summary": "VCS status"
}
```

## /api/vcs/branch

<a id="vcs.branch.list"></a>

### GET /api/vcs/branch — vcs.branch.list

```json
{
  "tags": [
    "vcs"
  ],
  "operationId": "vcs.branch.list",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "search",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    },
    {
      "name": "limit",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/Vcs.BranchList"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List local and remote branches available at the requested location.",
  "summary": "VCS branches"
}
```

## /api/vcs/diff

<a id="vcs.diff"></a>

### GET /api/vcs/diff — vcs.diff

```json
{
  "tags": [
    "vcs"
  ],
  "operationId": "vcs.diff",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    },
    {
      "name": "mode",
      "in": "query",
      "schema": {
        "$ref": "#/components/schemas/Vcs.Mode"
      },
      "required": true
    },
    {
      "name": "base",
      "in": "query",
      "schema": {
        "type": "string"
      },
      "required": false
    },
    {
      "name": "context",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/FileDiff.Info"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Diff HEAD to the working copy (working), the base merge-base to the working copy (branch), or the base merge-base to HEAD (committed). Omitting base preserves repository-default comparison; supplying it overrides the comparison without saving it.",
  "summary": "VCS diff"
}
```

## /api/debug/location

<a id="debug.location.list"></a>

### GET /api/debug/location — debug.location.list

```json
{
  "tags": [
    "debug"
  ],
  "operationId": "debug.location.list",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Location.PublicRef"
            }
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "List locations currently loaded by the server.",
  "summary": "List loaded locations"
}
```

<a id="debug.location.evict"></a>

### DELETE /api/debug/location — debug.location.evict

```json
{
  "tags": [
    "debug"
  ],
  "operationId": "debug.location.evict",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Dispose the requested location's cached services so its next use boots them fresh.",
  "summary": "Evict a loaded location"
}
```

## /api/experimental/migration/v1

<a id="experimental.migration.v1.status"></a>

### GET /api/experimental/migration/v1 — experimental.migration.v1.status

```json
{
  "tags": [
    "migration"
  ],
  "operationId": "experimental.migration.v1.status",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "anyOf": [
              {
                "type": "object",
                "properties": {
                  "status": {
                    "type": "string",
                    "enum": [
                      "required",
                      "completed"
                    ]
                  }
                },
                "required": [
                  "status"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "status": {
                    "type": "string",
                    "enum": [
                      "running"
                    ]
                  },
                  "progress": {
                    "type": "object",
                    "properties": {
                      "label": {
                        "type": "string"
                      },
                      "numerator": {
                        "anyOf": [
                          {
                            "type": "integer",
                            "minimum": 0
                          },
                          {
                            "type": "null"
                          }
                        ]
                      },
                      "denominator": {
                        "anyOf": [
                          {
                            "type": "integer",
                            "minimum": 0
                          },
                          {
                            "type": "null"
                          }
                        ]
                      }
                    },
                    "required": [
                      "label"
                    ],
                    "additionalProperties": false
                  }
                },
                "required": [
                  "status",
                  "progress"
                ],
                "additionalProperties": false
              },
              {
                "type": "object",
                "properties": {
                  "status": {
                    "type": "string",
                    "enum": [
                      "error"
                    ]
                  },
                  "error": {
                    "type": "string"
                  }
                },
                "required": [
                  "status",
                  "error"
                ],
                "additionalProperties": false
              }
            ]
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Return the progress of the V1 to V2 session history migration.",
  "summary": "Get V1 migration status"
}
```

## /api/websearch/provider

<a id="websearch.providers"></a>

### GET /api/websearch/provider — websearch.providers

```json
{
  "tags": [
    "websearch"
  ],
  "operationId": "websearch.providers",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/WebSearch.Provider"
                }
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Return the registered web search providers.",
  "summary": "List web search providers"
}
```

## /api/websearch

<a id="websearch.query"></a>

### POST /api/websearch — websearch.query

```json
{
  "tags": [
    "websearch"
  ],
  "operationId": "websearch.query",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "location": {
                "$ref": "#/components/schemas/Location.PublicRef"
              },
              "data": {
                "$ref": "#/components/schemas/WebSearch.ResponseEncoded"
              }
            },
            "required": [
              "location",
              "data"
            ],
            "additionalProperties": false
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    },
    "503": {
      "description": "ServiceUnavailableError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ServiceUnavailableErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Run one web search through the selected provider. Specify a provider to override the configured default.",
  "summary": "Search the web",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string"
            },
            "providerID": {
              "$ref": "#/components/schemas/WebSearch.ID"
            }
          },
          "required": [
            "query"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": true
  }
}
```

## /api/config

<a id="config.get"></a>

### GET /api/config — config.get

```json
{
  "tags": [
    "config"
  ],
  "operationId": "config.get",
  "parameters": [
    {
      "name": "location",
      "in": "query",
      "schema": {
        "anyOf": [
          {
            "type": "object",
            "properties": {
              "directory": {
                "anyOf": [
                  {
                    "type": "string"
                  },
                  {
                    "type": "null"
                  }
                ]
              }
            },
            "additionalProperties": false
          },
          {
            "type": "null"
          }
        ]
      },
      "required": false,
      "style": "deepObject",
      "explode": true
    }
  ],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Config.Entry"
            }
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Return configuration documents and discovery sources for the requested location, from lowest to highest priority.",
  "summary": "Get configuration"
}
```

## /api/config/shell

<a id="config.shells"></a>

### GET /api/config/shell — config.shells

```json
{
  "tags": [
    "config"
  ],
  "operationId": "config.shells",
  "parameters": [],
  "security": [],
  "responses": {
    "200": {
      "description": "Success",
      "content": {
        "application/json": {
          "schema": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ConfigShell.Option"
            }
          }
        }
      }
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Return shells available to terminal and agent execution.",
  "summary": "List available shells"
}
```

## /api/experimental/config

<a id="experimental.config.update"></a>

### PATCH /api/experimental/config — experimental.config.update

```json
{
  "tags": [
    "config"
  ],
  "operationId": "experimental.config.update",
  "parameters": [],
  "security": [],
  "responses": {
    "204": {
      "description": "<No Content>"
    },
    "400": {
      "description": "InvalidRequestError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/InvalidRequestErrorEncoded"
          }
        }
      }
    },
    "401": {
      "description": "UnauthorizedError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/UnauthorizedErrorEncoded"
          }
        }
      }
    },
    "404": {
      "description": "LocationNotFoundError",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/LocationNotFoundErrorEncoded"
          }
        }
      }
    }
  },
  "description": "Patch supported fields in the highest-precedence global configuration document.",
  "summary": "Update global configuration",
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Config.Patch"
        }
      }
    },
    "required": true
  }
}
```

<a id="schemas"></a>

## Components: schemas

<a id="schema-AbsolutePath"></a>

### AbsolutePath

```json
{
  "type": "string"
}
```

<a id="schema-Agent.Color"></a>

### Agent.Color

```json
{
  "type": "string"
}
```

<a id="schema-Agent.ID"></a>

### Agent.ID

```json
{
  "type": "string"
}
```

<a id="schema-Agent.Info"></a>

### Agent.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Agent.ID"
    },
    "name": {
      "type": "string"
    },
    "model": {
      "$ref": "#/components/schemas/Model.Ref"
    },
    "request": {
      "$ref": "#/components/schemas/Provider.Request"
    },
    "system": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mode": {
      "type": "string",
      "enum": [
        "subagent",
        "primary",
        "all"
      ]
    },
    "hidden": {
      "type": "boolean"
    },
    "color": {
      "$ref": "#/components/schemas/Agent.Color"
    },
    "steps": {
      "type": "integer",
      "exclusiveMinimum": 0
    },
    "permissions": {
      "$ref": "#/components/schemas/Permission.Ruleset"
    }
  },
  "required": [
    "id",
    "name",
    "request",
    "mode",
    "hidden",
    "permissions"
  ],
  "additionalProperties": false
}
```

<a id="schema-AgentNotFoundErrorEncoded"></a>

### AgentNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "AgentNotFoundError"
      ]
    },
    "agentID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "agentID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Command.Info"></a>

### Command.Info

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-CommandExecutionErrorEncoded"></a>

### CommandExecutionErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "CommandExecutionError"
      ]
    },
    "command": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "command",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-CommandNotFoundErrorEncoded"></a>

### CommandNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "CommandNotFoundError"
      ]
    },
    "command": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "command",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.AgentEncoded"></a>

### Config.AgentEncoded

```json
{
  "type": "object",
  "properties": {
    "model": {
      "anyOf": [
        {
          "type": "string",
          "pattern": "^[^/#]+\\/[^#]+(?:#[^#]+)?$"
        },
        {
          "type": "object",
          "properties": {
            "providerID": {
              "type": "string",
              "pattern": "^[^/#]+$"
            },
            "model": {
              "type": "string",
              "pattern": "^[^#]+$"
            },
            "variant": {
              "type": "string",
              "pattern": "^[^#]+$"
            }
          },
          "required": [
            "providerID",
            "model"
          ],
          "additionalProperties": false
        }
      ]
    },
    "request": {
      "type": "object",
      "properties": {
        "headers": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "body": {
          "type": "object"
        }
      },
      "additionalProperties": false
    },
    "system": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mode": {
      "type": "string",
      "enum": [
        "subagent",
        "primary",
        "all"
      ]
    },
    "hidden": {
      "type": "boolean"
    },
    "color": {
      "type": "string",
      "pattern": "^#[0-9a-fA-F]{6}$"
    },
    "steps": {
      "type": "integer",
      "exclusiveMinimum": 0
    },
    "disabled": {
      "type": "boolean"
    },
    "permissions": {
      "$ref": "#/components/schemas/Permission.Ruleset"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.CommandEncoded"></a>

### Config.CommandEncoded

```json
{
  "type": "object",
  "properties": {
    "template": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "agent": {
      "type": "string"
    },
    "model": {
      "anyOf": [
        {
          "type": "string",
          "pattern": "^[^/#]+\\/[^#]+(?:#[^#]+)?$"
        },
        {
          "type": "object",
          "properties": {
            "providerID": {
              "type": "string",
              "pattern": "^[^/#]+$"
            },
            "model": {
              "type": "string",
              "pattern": "^[^#]+$"
            },
            "variant": {
              "type": "string",
              "pattern": "^[^#]+$"
            }
          },
          "required": [
            "providerID",
            "model"
          ],
          "additionalProperties": false
        }
      ]
    },
    "subagent": {
      "type": "boolean"
    },
    "subtask": {
      "type": "boolean",
      "description": "Deprecated alias for subagent."
    }
  },
  "required": [
    "template"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.DirectoryEncoded"></a>

### Config.DirectoryEncoded

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "directory"
      ]
    },
    "path": {
      "$ref": "#/components/schemas/AbsolutePath"
    }
  },
  "required": [
    "type",
    "path"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.DocumentEncoded"></a>

### Config.DocumentEncoded

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "document"
      ]
    },
    "path": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "info": {
      "$ref": "#/components/schemas/Config.InfoEncoded"
    }
  },
  "required": [
    "type",
    "info"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.Entry"></a>

### Config.Entry

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Config.DocumentEncoded"
    },
    {
      "$ref": "#/components/schemas/Config.DirectoryEncoded"
    }
  ]
}
```

<a id="schema-Config.Formatter.EntryEncoded"></a>

### Config.Formatter.EntryEncoded

```json
{
  "type": "object",
  "properties": {
    "disabled": {
      "type": "boolean"
    },
    "command": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "environment": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "extensions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.InfoEncoded"></a>

### Config.InfoEncoded

```json
{
  "type": "object",
  "properties": {
    "$schema": {
      "type": "string"
    },
    "shell": {
      "type": "string"
    },
    "model": {
      "anyOf": [
        {
          "type": "string",
          "pattern": "^[^/#]+\\/[^#]+(?:#[^#]+)?$"
        },
        {
          "type": "object",
          "properties": {
            "providerID": {
              "type": "string",
              "pattern": "^[^/#]+$"
            },
            "model": {
              "type": "string",
              "pattern": "^[^#]+$"
            },
            "variant": {
              "type": "string",
              "pattern": "^[^#]+$"
            }
          },
          "required": [
            "providerID",
            "model"
          ],
          "additionalProperties": false
        }
      ]
    },
    "default_agent": {
      "type": "string"
    },
    "update": {
      "type": "string",
      "enum": [
        "disable",
        "notify",
        "auto"
      ]
    },
    "share": {
      "type": "string",
      "enum": [
        "manual",
        "auto",
        "disabled"
      ]
    },
    "enterprise": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "username": {
      "type": "string"
    },
    "permissions": {
      "$ref": "#/components/schemas/Permission.Ruleset"
    },
    "policies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string",
            "enum": [
              "provider.use",
              "tool.use",
              "integration.use"
            ]
          },
          "resource": {
            "type": "string"
          },
          "effect": {
            "type": "string",
            "enum": [
              "allow",
              "deny"
            ]
          }
        },
        "required": [
          "action",
          "resource",
          "effect"
        ],
        "additionalProperties": false
      }
    },
    "agents": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/components/schemas/Config.AgentEncoded"
      }
    },
    "snapshots": {
      "type": "boolean"
    },
    "watcher": {
      "type": "object",
      "properties": {
        "ignore": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "additionalProperties": false
    },
    "formatter": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/components/schemas/Config.Formatter.EntryEncoded"
          }
        }
      ]
    },
    "lsp": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "object",
          "additionalProperties": {
            "anyOf": [
              {
                "type": "object",
                "properties": {
                  "disabled": {
                    "type": "boolean",
                    "enum": [
                      true
                    ]
                  }
                },
                "required": [
                  "disabled"
                ],
                "additionalProperties": false
              },
              {
                "$ref": "#/components/schemas/Config.LSP.ServerEncoded"
              }
            ]
          }
        }
      ]
    },
    "media": {
      "type": "object",
      "properties": {
        "image": {
          "type": "object",
          "properties": {
            "auto_resize": {
              "type": "boolean"
            },
            "max_width": {
              "type": "integer",
              "exclusiveMinimum": 0
            },
            "max_height": {
              "type": "integer",
              "exclusiveMinimum": 0
            },
            "max_base64_bytes": {
              "type": "integer",
              "exclusiveMinimum": 0
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    },
    "tool_output": {
      "type": "object",
      "properties": {
        "max_lines": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "max_bytes": {
          "type": "integer",
          "exclusiveMinimum": 0
        }
      },
      "additionalProperties": false
    },
    "mcp": {
      "type": "object",
      "properties": {
        "timeout": {
          "type": "object",
          "properties": {
            "startup": {
              "type": "integer",
              "exclusiveMinimum": 0
            },
            "catalog": {
              "type": "integer",
              "exclusiveMinimum": 0
            },
            "execution": {
              "type": "integer",
              "exclusiveMinimum": 0
            }
          },
          "additionalProperties": false
        },
        "servers": {
          "type": "object",
          "additionalProperties": {
            "anyOf": [
              {
                "$ref": "#/components/schemas/Mcp.LocalConfigEncoded"
              },
              {
                "$ref": "#/components/schemas/Mcp.RemoteConfigEncoded"
              }
            ]
          }
        }
      },
      "additionalProperties": false
    },
    "compaction": {
      "type": "object",
      "properties": {
        "auto": {
          "type": "boolean"
        },
        "keep": {
          "type": "object",
          "properties": {
            "tokens": {
              "type": "integer",
              "minimum": 0
            }
          },
          "additionalProperties": false
        },
        "buffer": {
          "type": "integer",
          "minimum": 0
        }
      },
      "additionalProperties": false
    },
    "skills": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "commands": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/components/schemas/Config.CommandEncoded"
      }
    },
    "instructions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "references": {
      "type": "object",
      "additionalProperties": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "$ref": "#/components/schemas/Config.Reference.GitEncoded"
          },
          {
            "$ref": "#/components/schemas/Config.Reference.LocalEncoded"
          }
        ]
      }
    },
    "websearch": {
      "anyOf": [
        {
          "type": "boolean",
          "enum": [
            false
          ]
        },
        {
          "$ref": "#/components/schemas/ConfigWebSearch.InfoEncoded"
        }
      ]
    },
    "plugins": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "$ref": "#/components/schemas/Config.Plugin.EntryEncoded"
          }
        ]
      }
    },
    "worktree": {
      "$ref": "#/components/schemas/Config.Worktree"
    },
    "warming": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "$ref": "#/components/schemas/Config.WarmingEncoded"
        }
      ]
    },
    "providers": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/components/schemas/Config.ProviderEncoded"
      }
    },
    "experimental": {
      "type": "object",
      "properties": {
        "portable_shell_scanner": {
          "type": "boolean"
        },
        "subagent_depth": {
          "type": "integer",
          "minimum": 0
        },
        "policies": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "action": {
                "type": "string",
                "enum": [
                  "provider.use",
                  "tool.use",
                  "integration.use"
                ]
              },
              "resource": {
                "type": "string"
              },
              "effect": {
                "type": "string",
                "enum": [
                  "allow",
                  "deny"
                ]
              }
            },
            "required": [
              "action",
              "resource",
              "effect"
            ],
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.LSP.ServerEncoded"></a>

### Config.LSP.ServerEncoded

```json
{
  "type": "object",
  "properties": {
    "command": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "extensions": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "disabled": {
      "type": "boolean"
    },
    "env": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "initialization": {
      "type": "object"
    }
  },
  "required": [
    "command"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.Model.Capabilities"></a>

### Config.Model.Capabilities

```json
{
  "type": "object",
  "properties": {
    "tools": {
      "type": "boolean"
    },
    "input": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "output": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.Model.CostEncoded"></a>

### Config.Model.CostEncoded

```json
{
  "type": "object",
  "properties": {
    "tier": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "context"
          ]
        },
        "size": {
          "type": "integer"
        }
      },
      "required": [
        "type",
        "size"
      ],
      "additionalProperties": false
    },
    "input": {
      "$ref": "#/components/schemas/Money.USDPerMillionTokens"
    },
    "output": {
      "$ref": "#/components/schemas/Money.USDPerMillionTokens"
    },
    "cache": {
      "type": "object",
      "properties": {
        "read": {
          "$ref": "#/components/schemas/Money.USDPerMillionTokens"
        },
        "write": {
          "$ref": "#/components/schemas/Money.USDPerMillionTokens"
        }
      },
      "additionalProperties": false
    }
  },
  "required": [
    "input",
    "output"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.Model.Settings"></a>

### Config.Model.Settings

```json
{
  "type": "object",
  "properties": {
    "compaction": {
      "$ref": "#/components/schemas/Provider.Compaction"
    },
    "encoding": {
      "$ref": "#/components/schemas/Provider.Encoding"
    }
  },
  "allOf": [
    {
      "type": "object",
      "additionalProperties": {
        "anyOf": [
          {},
          {
            "type": "null"
          }
        ]
      }
    }
  ]
}
```

<a id="schema-Config.ModelEncoded"></a>

### Config.ModelEncoded

```json
{
  "type": "object",
  "properties": {
    "modelID": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "compatibility": {
      "$ref": "#/components/schemas/Model.Compatibility"
    },
    "package": {
      "type": "string"
    },
    "settings": {
      "$ref": "#/components/schemas/Config.Model.Settings"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "body": {
      "type": "object"
    },
    "capabilities": {
      "$ref": "#/components/schemas/Config.Model.Capabilities"
    },
    "variants": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string"
          },
          "settings": {
            "$ref": "#/components/schemas/Config.Model.Settings"
          },
          "headers": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "body": {
            "type": "object"
          }
        },
        "required": [
          "id"
        ],
        "additionalProperties": false
      }
    },
    "cost": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/Config.Model.CostEncoded"
        },
        {
          "type": "array",
          "items": {
            "$ref": "#/components/schemas/Config.Model.CostEncoded"
          }
        }
      ]
    },
    "disabled": {
      "type": "boolean"
    },
    "limit": {
      "type": "object",
      "properties": {
        "context": {
          "type": "integer"
        },
        "input": {
          "type": "integer"
        },
        "output": {
          "type": "integer"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.Patch"></a>

### Config.Patch

```json
{
  "type": "object",
  "properties": {
    "shell": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "shell"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.Plugin.EntryEncoded"></a>

### Config.Plugin.EntryEncoded

```json
{
  "type": "object",
  "properties": {
    "package": {
      "type": "string"
    },
    "options": {
      "type": "object"
    }
  },
  "required": [
    "package"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.Provider.Settings"></a>

### Config.Provider.Settings

```json
{
  "type": "object",
  "properties": {
    "timeout": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "headerTimeout": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "chunkTimeout": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "compaction": {
      "$ref": "#/components/schemas/Provider.Compaction"
    },
    "transport": {
      "$ref": "#/components/schemas/Provider.Transport"
    },
    "encoding": {
      "$ref": "#/components/schemas/Provider.Encoding"
    }
  },
  "allOf": [
    {
      "type": "object",
      "additionalProperties": {
        "anyOf": [
          {},
          {
            "type": "null"
          }
        ]
      }
    }
  ]
}
```

<a id="schema-Config.ProviderEncoded"></a>

### Config.ProviderEncoded

```json
{
  "type": "object",
  "properties": {
    "canonical": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "name": {
      "type": "string"
    },
    "env": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "package": {
      "type": "string"
    },
    "compatibility": {
      "$ref": "#/components/schemas/Provider.Compatibility"
    },
    "settings": {
      "$ref": "#/components/schemas/Config.Provider.Settings"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "body": {
      "type": "object"
    },
    "models": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/components/schemas/Config.ModelEncoded"
      }
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.Reference.GitEncoded"></a>

### Config.Reference.GitEncoded

```json
{
  "type": "object",
  "properties": {
    "repository": {
      "type": "string"
    },
    "branch": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "hidden": {
      "type": "boolean"
    }
  },
  "required": [
    "repository"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.Reference.LocalEncoded"></a>

### Config.Reference.LocalEncoded

```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "hidden": {
      "type": "boolean"
    }
  },
  "required": [
    "path"
  ],
  "additionalProperties": false
}
```

<a id="schema-Config.WarmingEncoded"></a>

### Config.WarmingEncoded

```json
{
  "type": "object",
  "properties": {
    "prompt": {
      "type": "string"
    },
    "interval": {
      "type": "string"
    },
    "duration": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Config.Worktree"></a>

### Config.Worktree

```json
{
  "type": "object",
  "properties": {
    "directory": {
      "type": "string"
    }
  },
  "required": [
    "directory"
  ],
  "additionalProperties": false
}
```

<a id="schema-ConfigShell.Option"></a>

### ConfigShell.Option

```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "acceptable": {
      "type": "boolean"
    }
  },
  "required": [
    "path",
    "name",
    "acceptable"
  ],
  "additionalProperties": false
}
```

<a id="schema-ConfigWebSearch.InfoEncoded"></a>

### ConfigWebSearch.InfoEncoded

```json
{
  "type": "object",
  "properties": {
    "provider": {
      "anyOf": [
        {
          "type": "string",
          "enum": [
            "random"
          ],
          "description": "Reuse a randomly selected provider until it is rate limited, then switch to another available provider."
        },
        {
          "$ref": "#/components/schemas/WebSearch.ID"
        }
      ]
    }
  },
  "required": [
    "provider"
  ],
  "additionalProperties": false
}
```

<a id="schema-ConflictErrorEncoded"></a>

### ConflictErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "ConflictError"
      ]
    },
    "message": {
      "type": "string"
    },
    "resource": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Connection.CredentialInfo"></a>

### Connection.CredentialInfo

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "credential"
      ]
    },
    "id": {
      "$ref": "#/components/schemas/Credential.ID"
    },
    "label": {
      "type": "string"
    },
    "method": {
      "type": "string",
      "enum": [
        "key",
        "oauth",
        "external"
      ]
    },
    "status": {
      "$ref": "#/components/schemas/Connection.Status"
    }
  },
  "required": [
    "type",
    "id",
    "label",
    "method"
  ],
  "additionalProperties": false
}
```

<a id="schema-Connection.EnvInfo"></a>

### Connection.EnvInfo

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "env"
      ]
    },
    "name": {
      "type": "string"
    },
    "status": {
      "$ref": "#/components/schemas/Connection.Status"
    }
  },
  "required": [
    "type",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-Connection.Info"></a>

### Connection.Info

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Connection.CredentialInfo"
    },
    {
      "$ref": "#/components/schemas/Connection.EnvInfo"
    }
  ]
}
```

<a id="schema-Connection.Status"></a>

### Connection.Status

```json
{
  "type": "object",
  "properties": {
    "status": {
      "anyOf": [
        {
          "type": "string",
          "enum": [
            "needs_auth"
          ]
        }
      ]
    },
    "message": {
      "type": "string"
    },
    "url": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Credential.CreateInput"></a>

### Credential.CreateInput

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Credential.ID"
    },
    "integrationID": {
      "$ref": "#/components/schemas/Integration.ID"
    },
    "label": {
      "type": "string"
    },
    "value": {
      "$ref": "#/components/schemas/Credential.Value"
    },
    "activate": {
      "type": "boolean"
    }
  },
  "required": [
    "integrationID",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-Credential.Entry"></a>

### Credential.Entry

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Credential.ID"
    },
    "integrationID": {
      "$ref": "#/components/schemas/Integration.ID"
    },
    "label": {
      "type": "string"
    },
    "active": {
      "type": "boolean"
    },
    "value": {
      "$ref": "#/components/schemas/Credential.Value"
    }
  },
  "required": [
    "id",
    "integrationID",
    "label",
    "active",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-Credential.External"></a>

### Credential.External

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "external"
      ]
    },
    "methodID": {
      "$ref": "#/components/schemas/Integration.MethodID"
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "type",
    "methodID"
  ],
  "additionalProperties": false
}
```

<a id="schema-Credential.ID"></a>

### Credential.ID

```json
{
  "type": "string"
}
```

<a id="schema-Credential.Key"></a>

### Credential.Key

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "key"
      ]
    },
    "key": {
      "type": "string"
    },
    "metadata": {
      "type": "object"
    },
    "configuration": {
      "$ref": "#/components/schemas/Form.Answer_1"
    }
  },
  "required": [
    "type",
    "key"
  ],
  "additionalProperties": false
}
```

<a id="schema-Credential.OAuth"></a>

### Credential.OAuth

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "oauth"
      ]
    },
    "methodID": {
      "$ref": "#/components/schemas/Integration.MethodID"
    },
    "refresh": {
      "type": "string"
    },
    "access": {
      "type": "string"
    },
    "expires": {
      "type": "integer",
      "minimum": 0
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "type",
    "methodID",
    "refresh",
    "access",
    "expires"
  ],
  "additionalProperties": false
}
```

<a id="schema-Credential.Value"></a>

### Credential.Value

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Credential.OAuth"
    },
    {
      "$ref": "#/components/schemas/Credential.Key"
    },
    {
      "$ref": "#/components/schemas/Credential.External"
    }
  ]
}
```

<a id="schema-Event.SeqEncoded"></a>

### Event.SeqEncoded

```json
{
  "type": "string"
}
```

<a id="schema-FileDiff.Info"></a>

### FileDiff.Info

```json
{
  "type": "object",
  "properties": {
    "file": {
      "type": "string"
    },
    "patch": {
      "type": "string"
    },
    "additions": {
      "type": "integer",
      "minimum": 0
    },
    "deletions": {
      "type": "integer",
      "minimum": 0
    },
    "status": {
      "type": "string",
      "enum": [
        "added",
        "deleted",
        "modified"
      ]
    }
  },
  "required": [
    "file",
    "patch",
    "additions",
    "deletions",
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-FileNotFoundErrorEncoded"></a>

### FileNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "FileNotFoundError"
      ]
    },
    "path": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "path",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-FileSystem.Entry"></a>

### FileSystem.Entry

```json
{
  "type": "object",
  "properties": {
    "path": {
      "$ref": "#/components/schemas/RelativePath"
    },
    "type": {
      "type": "string",
      "enum": [
        "file",
        "directory"
      ]
    }
  },
  "required": [
    "path",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-FileSystem.Write"></a>

### FileSystem.Write

```json
{
  "type": "object",
  "properties": {
    "path": {
      "$ref": "#/components/schemas/AbsolutePath"
    }
  },
  "required": [
    "path"
  ],
  "additionalProperties": false
}
```

<a id="schema-ForbiddenErrorEncoded"></a>

### ForbiddenErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "ForbiddenError"
      ]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Answer"></a>

### Form.Answer

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/components/schemas/Form.Value"
  }
}
```

<a id="schema-Form.Answer_1"></a>

### Form.Answer_1

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/components/schemas/Form.Value"
  }
}
```

<a id="schema-Form.BooleanField"></a>

### Form.BooleanField

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "required": {
      "type": "boolean"
    },
    "hidden": {
      "type": "boolean"
    },
    "when": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.When"
      }
    },
    "type": {
      "type": "string",
      "enum": [
        "boolean"
      ]
    },
    "default": {
      "type": "boolean"
    }
  },
  "required": [
    "key",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.CreatePayload"></a>

### Form.CreatePayload

```json
{
  "type": "object",
  "properties": {
    "id": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/Form.ID"
        },
        {
          "type": "null"
        }
      ]
    },
    "title": {
      "type": "string"
    },
    "metadata": {
      "$ref": "#/components/schemas/Form.Metadata"
    },
    "fields": {
      "$ref": "#/components/schemas/Form.Fields"
    }
  },
  "required": [
    "title",
    "fields"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Detail"></a>

### Form.Detail

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Form.ID"
    },
    "sessionID": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "metadata": {
      "$ref": "#/components/schemas/Form.Metadata"
    },
    "fields": {
      "$ref": "#/components/schemas/Form.Fields"
    },
    "state": {
      "$ref": "#/components/schemas/Form.State"
    }
  },
  "required": [
    "id",
    "sessionID",
    "title",
    "fields",
    "state"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.ExternalField"></a>

### Form.ExternalField

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "type": {
      "type": "string",
      "enum": [
        "external"
      ]
    },
    "url": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "key",
    "type",
    "url"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Field"></a>

### Form.Field

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Form.StringField"
    },
    {
      "$ref": "#/components/schemas/Form.NumberField"
    },
    {
      "$ref": "#/components/schemas/Form.IntegerField"
    },
    {
      "$ref": "#/components/schemas/Form.BooleanField"
    },
    {
      "$ref": "#/components/schemas/Form.MultiselectField"
    },
    {
      "$ref": "#/components/schemas/Form.ExternalField"
    }
  ]
}
```

<a id="schema-Form.Fields"></a>

### Form.Fields

```json
{
  "type": "array",
  "prefixItems": [
    {
      "$ref": "#/components/schemas/Form.Field"
    }
  ],
  "minItems": 1,
  "items": {
    "$ref": "#/components/schemas/Form.Field"
  }
}
```

<a id="schema-Form.Fields_1"></a>

### Form.Fields_1

```json
{
  "type": "array",
  "prefixItems": [
    {
      "$ref": "#/components/schemas/Form.Field"
    }
  ],
  "minItems": 1,
  "items": {
    "$ref": "#/components/schemas/Form.Field"
  }
}
```

<a id="schema-Form.Fields_2"></a>

### Form.Fields_2

```json
{
  "type": "array",
  "prefixItems": [
    {
      "$ref": "#/components/schemas/Form.Field"
    }
  ],
  "minItems": 1,
  "items": {
    "$ref": "#/components/schemas/Form.Field"
  }
}
```

<a id="schema-Form.Fields_3"></a>

### Form.Fields_3

```json
{
  "type": "array",
  "prefixItems": [
    {
      "$ref": "#/components/schemas/Form.Field"
    }
  ],
  "minItems": 1,
  "items": {
    "$ref": "#/components/schemas/Form.Field"
  }
}
```

<a id="schema-Form.ID"></a>

### Form.ID

```json
{
  "type": "string",
  "pattern": "^frm_"
}
```

<a id="schema-Form.Info"></a>

### Form.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Form.ID"
    },
    "sessionID": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "metadata": {
      "$ref": "#/components/schemas/Form.Metadata"
    },
    "fields": {
      "$ref": "#/components/schemas/Form.Fields"
    }
  },
  "required": [
    "id",
    "sessionID",
    "title",
    "fields"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.IntegerField"></a>

### Form.IntegerField

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "required": {
      "type": "boolean"
    },
    "hidden": {
      "type": "boolean"
    },
    "when": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.When"
      }
    },
    "type": {
      "type": "string",
      "enum": [
        "integer"
      ]
    },
    "minimum": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    },
    "maximum": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    },
    "default": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    }
  },
  "required": [
    "key",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Metadata"></a>

### Form.Metadata

```json
{
  "type": "object"
}
```

<a id="schema-Form.MultiselectField"></a>

### Form.MultiselectField

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "required": {
      "type": "boolean"
    },
    "hidden": {
      "type": "boolean"
    },
    "when": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.When"
      }
    },
    "type": {
      "type": "string",
      "enum": [
        "multiselect"
      ]
    },
    "options": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.Option"
      }
    },
    "minItems": {
      "type": "integer",
      "minimum": 0
    },
    "maxItems": {
      "type": "integer",
      "minimum": 0
    },
    "custom": {
      "type": "boolean"
    },
    "default": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "key",
    "type",
    "options"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.NumberField"></a>

### Form.NumberField

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "required": {
      "type": "boolean"
    },
    "hidden": {
      "type": "boolean"
    },
    "when": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.When"
      }
    },
    "type": {
      "type": "string",
      "enum": [
        "number"
      ]
    },
    "minimum": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    },
    "maximum": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    },
    "default": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    }
  },
  "required": [
    "key",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Option"></a>

### Form.Option

```json
{
  "type": "object",
  "properties": {
    "value": {
      "type": "string"
    },
    "label": {
      "type": "string"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "value",
    "label"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Reply"></a>

### Form.Reply

```json
{
  "type": "object",
  "properties": {
    "answer": {
      "$ref": "#/components/schemas/Form.Answer"
    }
  },
  "required": [
    "answer"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.State"></a>

### Form.State

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "pending"
          ]
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "answered"
          ]
        },
        "answer": {
          "$ref": "#/components/schemas/Form.Answer"
        }
      },
      "required": [
        "status",
        "answer"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "cancelled"
          ]
        },
        "message": {
          "type": "string"
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Form.StringField"></a>

### Form.StringField

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "required": {
      "type": "boolean"
    },
    "hidden": {
      "type": "boolean"
    },
    "when": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.When"
      }
    },
    "type": {
      "type": "string",
      "enum": [
        "string"
      ]
    },
    "format": {
      "type": "string",
      "enum": [
        "email",
        "uri",
        "date",
        "date-time"
      ]
    },
    "minLength": {
      "type": "integer",
      "minimum": 0
    },
    "maxLength": {
      "type": "integer",
      "minimum": 0
    },
    "pattern": {
      "type": "string"
    },
    "placeholder": {
      "type": "string"
    },
    "default": {
      "type": "string"
    },
    "options": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Form.Option"
      }
    },
    "custom": {
      "type": "boolean"
    }
  },
  "required": [
    "key",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Form.Value"></a>

### Form.Value

```json
{
  "anyOf": [
    {
      "type": "string"
    },
    {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    },
    {
      "type": "boolean"
    },
    {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  ]
}
```

<a id="schema-Form.When"></a>

### Form.When

```json
{
  "type": "object",
  "properties": {
    "key": {
      "type": "string"
    },
    "op": {
      "type": "string",
      "enum": [
        "eq",
        "neq"
      ]
    },
    "value": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "string",
              "enum": [
                "Infinity",
                "-Infinity",
                "NaN"
              ]
            }
          ]
        },
        {
          "type": "boolean"
        }
      ]
    }
  },
  "required": [
    "key",
    "op",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-FormAlreadySettledErrorEncoded"></a>

### FormAlreadySettledErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "FormAlreadySettledError"
      ]
    },
    "id": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "id",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-FormInvalidAnswerErrorEncoded"></a>

### FormInvalidAnswerErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "FormInvalidAnswerError"
      ]
    },
    "id": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "id",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-FormNotFoundErrorEncoded"></a>

### FormNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "FormNotFoundError"
      ]
    },
    "id": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "id",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-GenerateTextResponse"></a>

### GenerateTextResponse

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string"
        }
      },
      "required": [
        "text"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "data"
  ],
  "additionalProperties": false
}
```

<a id="schema-InstructionEntry.Info"></a>

### InstructionEntry.Info

```json
{
  "type": "object",
  "properties": {
    "key": {
      "$ref": "#/components/schemas/InstructionEntry.Key"
    },
    "value": {
      "description": "JSON value attached to the session's instructions"
    }
  },
  "required": [
    "key",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="schema-InstructionEntry.Key"></a>

### InstructionEntry.Key

```json
{
  "type": "string",
  "pattern": "^[a-z0-9][a-z0-9._-]*$",
  "description": "Instruction entry key (lowercase alphanumerics plus . _ -)"
}
```

<a id="schema-InstructionEntryValueTooLargeErrorEncoded"></a>

### InstructionEntryValueTooLargeErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "InstructionEntryValueTooLargeError"
      ]
    },
    "actualBytes": {
      "type": "integer"
    },
    "maxBytes": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "actualBytes",
    "maxBytes",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.AttemptEncoded"></a>

### Integration.AttemptEncoded

```json
{
  "type": "object",
  "properties": {
    "attemptID": {
      "$ref": "#/components/schemas/Integration.AttemptID"
    },
    "url": {
      "type": "string"
    },
    "instructions": {
      "type": "string"
    },
    "mode": {
      "type": "string",
      "enum": [
        "auto",
        "code"
      ]
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "string",
              "enum": [
                "Infinity",
                "-Infinity",
                "NaN"
              ]
            }
          ]
        },
        "expires": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "string",
              "enum": [
                "Infinity",
                "-Infinity",
                "NaN"
              ]
            }
          ]
        }
      },
      "required": [
        "created",
        "expires"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "attemptID",
    "url",
    "instructions",
    "mode",
    "time"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.AttemptID"></a>

### Integration.AttemptID

```json
{
  "type": "string"
}
```

<a id="schema-Integration.AttemptStatus"></a>

### Integration.AttemptStatus

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "pending"
          ]
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "time"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "complete"
          ]
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "time"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "failed"
          ]
        },
        "message": {
          "type": "string"
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "message",
        "time"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "expired"
          ]
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "time"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Integration.CommandAttempt"></a>

### Integration.CommandAttempt

```json
{
  "type": "object",
  "properties": {
    "attemptID": {
      "$ref": "#/components/schemas/Integration.AttemptID"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "string",
              "enum": [
                "Infinity",
                "-Infinity",
                "NaN"
              ]
            }
          ]
        },
        "expires": {
          "anyOf": [
            {
              "type": "number"
            },
            {
              "type": "string",
              "enum": [
                "Infinity",
                "-Infinity",
                "NaN"
              ]
            }
          ]
        }
      },
      "required": [
        "created",
        "expires"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "attemptID",
    "time"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.CommandAttemptStatus"></a>

### Integration.CommandAttemptStatus

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "pending"
          ]
        },
        "message": {
          "type": "string"
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "time"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "complete"
          ]
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "time"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "failed"
          ]
        },
        "message": {
          "type": "string"
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "message",
        "time"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "expired"
          ]
        },
        "time": {
          "type": "object",
          "properties": {
            "created": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            },
            "expires": {
              "anyOf": [
                {
                  "type": "number"
                },
                {
                  "type": "string",
                  "enum": [
                    "Infinity",
                    "-Infinity",
                    "NaN"
                  ]
                }
              ]
            }
          },
          "required": [
            "created",
            "expires"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "time"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Integration.CommandMethod"></a>

### Integration.CommandMethod

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Integration.MethodID"
    },
    "type": {
      "type": "string",
      "enum": [
        "command"
      ]
    },
    "label": {
      "type": "string"
    },
    "command": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "id",
    "type",
    "label",
    "command"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.EnvMethod"></a>

### Integration.EnvMethod

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "env"
      ]
    },
    "names": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "type",
    "names"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.ExternalMethod"></a>

### Integration.ExternalMethod

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Integration.MethodID"
    },
    "type": {
      "type": "string",
      "enum": [
        "external"
      ]
    },
    "label": {
      "type": "string"
    },
    "form": {
      "$ref": "#/components/schemas/Form.Fields_3"
    }
  },
  "required": [
    "id",
    "type",
    "label"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.ID"></a>

### Integration.ID

```json
{
  "type": "string"
}
```

<a id="schema-Integration.Info"></a>

### Integration.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Integration.ID"
    },
    "name": {
      "type": "string"
    },
    "metadata": {
      "type": "object"
    },
    "methods": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Integration.Method"
      }
    },
    "connections": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Connection.Info"
      }
    }
  },
  "required": [
    "id",
    "name",
    "methods",
    "connections"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.KeyMethod"></a>

### Integration.KeyMethod

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "key"
      ]
    },
    "label": {
      "type": "string"
    },
    "form": {
      "$ref": "#/components/schemas/Form.Fields_2"
    }
  },
  "required": [
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Integration.Method"></a>

### Integration.Method

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Integration.OAuthMethod"
    },
    {
      "$ref": "#/components/schemas/Integration.CommandMethod"
    },
    {
      "$ref": "#/components/schemas/Integration.KeyMethod"
    },
    {
      "$ref": "#/components/schemas/Integration.ExternalMethod"
    },
    {
      "$ref": "#/components/schemas/Integration.EnvMethod"
    }
  ]
}
```

<a id="schema-Integration.MethodID"></a>

### Integration.MethodID

```json
{
  "type": "string"
}
```

<a id="schema-Integration.OAuthMethod"></a>

### Integration.OAuthMethod

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Integration.MethodID"
    },
    "type": {
      "type": "string",
      "enum": [
        "oauth"
      ]
    },
    "label": {
      "type": "string"
    },
    "form": {
      "$ref": "#/components/schemas/Form.Fields_1"
    }
  },
  "required": [
    "id",
    "type",
    "label"
  ],
  "additionalProperties": false
}
```

<a id="schema-IntegrationAttemptNotFoundErrorEncoded"></a>

### IntegrationAttemptNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "IntegrationAttemptNotFoundError"
      ]
    },
    "integrationID": {
      "type": "string"
    },
    "attemptID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "integrationID",
    "attemptID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-IntegrationMethodNotFoundErrorEncoded"></a>

### IntegrationMethodNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "IntegrationMethodNotFoundError"
      ]
    },
    "integrationID": {
      "type": "string"
    },
    "methodID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "integrationID",
    "methodID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-IntegrationNotFoundErrorEncoded"></a>

### IntegrationNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "IntegrationNotFoundError"
      ]
    },
    "integrationID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "integrationID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-InvalidCursorErrorEncoded"></a>

### InvalidCursorErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "InvalidCursorError"
      ]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-InvalidRequestErrorEncoded"></a>

### InvalidRequestErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "InvalidRequestError"
      ]
    },
    "message": {
      "type": "string"
    },
    "kind": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "field": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Location.PublicInfo"></a>

### Location.PublicInfo

```json
{
  "type": "object",
  "properties": {
    "directory": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "project": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/components/schemas/Project.ID"
        },
        "directory": {
          "$ref": "#/components/schemas/AbsolutePath"
        },
        "canonical": {
          "$ref": "#/components/schemas/AbsolutePath"
        }
      },
      "required": [
        "id",
        "directory",
        "canonical"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "directory",
    "project"
  ],
  "additionalProperties": false
}
```

<a id="schema-Location.PublicRef"></a>

### Location.PublicRef

```json
{
  "type": "object",
  "properties": {
    "directory": {
      "$ref": "#/components/schemas/AbsolutePath"
    }
  },
  "required": [
    "directory"
  ],
  "additionalProperties": false
}
```

<a id="schema-LocationNotFoundErrorEncoded"></a>

### LocationNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "LocationNotFoundError"
      ]
    },
    "location": {
      "$ref": "#/components/schemas/Location.PublicRef"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "location",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.LocalConfigEncoded"></a>

### Mcp.LocalConfigEncoded

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "local"
      ]
    },
    "command": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "cwd": {
      "type": "string"
    },
    "environment": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "disabled": {
      "type": "boolean"
    },
    "codemode": {
      "type": "boolean"
    },
    "timeout": {
      "type": "object",
      "properties": {
        "startup": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "catalog": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "execution": {
          "type": "integer",
          "exclusiveMinimum": 0
        }
      },
      "additionalProperties": false
    },
    "protocol": {
      "$ref": "#/components/schemas/Mcp.Protocol"
    }
  },
  "required": [
    "type",
    "command"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.OAuthConfigEncoded"></a>

### Mcp.OAuthConfigEncoded

```json
{
  "type": "object",
  "properties": {
    "client_id": {
      "type": "string"
    },
    "client_secret": {
      "type": "string"
    },
    "scope": {
      "type": "string"
    },
    "callback_port": {
      "type": "integer",
      "minimum": 1,
      "maximum": 65535
    },
    "redirect_uri": {
      "type": "string"
    },
    "auth_server_metadata_url": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Mcp.Protocol"></a>

### Mcp.Protocol

```json
{
  "type": "string",
  "enum": [
    "legacy",
    "auto",
    "2026-07-28"
  ],
  "description": "MCP protocol negotiation. \"legacy\" (default) opens with the initialize handshake and speaks protocol revisions up to 2025-11-25. \"auto\" probes for the 2026-07-28 revision and falls back to legacy when the server does not support it. \"2026-07-28\" requires that revision and fails otherwise."
}
```

<a id="schema-Mcp.RemoteConfigEncoded"></a>

### Mcp.RemoteConfigEncoded

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "remote"
      ]
    },
    "url": {
      "type": "string"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "oauth": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/Mcp.OAuthConfigEncoded"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "disabled": {
      "type": "boolean"
    },
    "codemode": {
      "type": "boolean"
    },
    "timeout": {
      "type": "object",
      "properties": {
        "startup": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "catalog": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "execution": {
          "type": "integer",
          "exclusiveMinimum": 0
        }
      },
      "additionalProperties": false
    },
    "protocol": {
      "$ref": "#/components/schemas/Mcp.Protocol"
    }
  },
  "required": [
    "type",
    "url"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Resource"></a>

### Mcp.Resource

```json
{
  "type": "object",
  "properties": {
    "server": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "uri": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mimeType": {
      "type": "string"
    }
  },
  "required": [
    "server",
    "name",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.ResourceCatalog"></a>

### Mcp.ResourceCatalog

```json
{
  "type": "object",
  "properties": {
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Mcp.Resource"
      }
    },
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Mcp.ResourceTemplate"
      }
    }
  },
  "required": [
    "resources",
    "templates"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.ResourceTemplate"></a>

### Mcp.ResourceTemplate

```json
{
  "type": "object",
  "properties": {
    "server": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "uriTemplate": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mimeType": {
      "type": "string"
    }
  },
  "required": [
    "server",
    "name",
    "uriTemplate"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Server"></a>

### Mcp.Server

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "status": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/Mcp.Status.Connected"
        },
        {
          "$ref": "#/components/schemas/Mcp.Status.Pending"
        },
        {
          "$ref": "#/components/schemas/Mcp.Status.Disabled"
        },
        {
          "$ref": "#/components/schemas/Mcp.Status.Failed"
        },
        {
          "$ref": "#/components/schemas/Mcp.Status.NeedsAuth"
        }
      ]
    },
    "integrationID": {
      "$ref": "#/components/schemas/Integration.ID"
    }
  },
  "required": [
    "name",
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Status.Connected"></a>

### Mcp.Status.Connected

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "connected"
      ]
    }
  },
  "required": [
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Status.Disabled"></a>

### Mcp.Status.Disabled

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "disabled"
      ]
    }
  },
  "required": [
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Status.Failed"></a>

### Mcp.Status.Failed

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "failed"
      ]
    },
    "error": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "error"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Status.NeedsAuth"></a>

### Mcp.Status.NeedsAuth

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "needs_auth"
      ]
    },
    "error": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "error"
  ],
  "additionalProperties": false
}
```

<a id="schema-Mcp.Status.Pending"></a>

### Mcp.Status.Pending

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "pending"
      ]
    }
  },
  "required": [
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-McpServerNotFoundErrorEncoded"></a>

### McpServerNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "McpServerNotFoundError"
      ]
    },
    "server": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "server",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-MessageNotFoundErrorEncoded"></a>

### MessageNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "MessageNotFoundError"
      ]
    },
    "sessionID": {
      "type": "string"
    },
    "messageID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "sessionID",
    "messageID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Model.CacheFormat"></a>

### Model.CacheFormat

```json
{
  "type": "string",
  "enum": [
    "anthropic",
    "alibaba"
  ]
}
```

<a id="schema-Model.Capabilities"></a>

### Model.Capabilities

```json
{
  "type": "object",
  "properties": {
    "tools": {
      "type": "boolean"
    },
    "input": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "output": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "tools",
    "input",
    "output"
  ],
  "additionalProperties": false
}
```

<a id="schema-Model.Compatibility"></a>

### Model.Compatibility

```json
{
  "type": "object",
  "properties": {
    "reasoningField": {
      "$ref": "#/components/schemas/Model.ReasoningField"
    },
    "requireReasoning": {
      "type": "boolean"
    },
    "maxTokensField": {
      "$ref": "#/components/schemas/Model.MaxTokensField"
    },
    "requireFinishReason": {
      "type": "boolean"
    },
    "requireAssistantAfterTool": {
      "type": "boolean"
    },
    "supportsPromptCacheKey": {
      "type": "boolean"
    },
    "cacheFormat": {
      "$ref": "#/components/schemas/Model.CacheFormat"
    },
    "supportsThinkingBlockBinding": {
      "type": "boolean"
    },
    "supportsEffortUpdates": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Model.Cost"></a>

### Model.Cost

```json
{
  "type": "object",
  "properties": {
    "tier": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "context"
          ]
        },
        "size": {
          "type": "integer"
        }
      },
      "required": [
        "type",
        "size"
      ],
      "additionalProperties": false
    },
    "input": {
      "$ref": "#/components/schemas/Money.USDPerMillionTokens"
    },
    "output": {
      "$ref": "#/components/schemas/Money.USDPerMillionTokens"
    },
    "cache": {
      "type": "object",
      "properties": {
        "read": {
          "$ref": "#/components/schemas/Money.USDPerMillionTokens"
        },
        "write": {
          "$ref": "#/components/schemas/Money.USDPerMillionTokens"
        }
      },
      "required": [
        "read",
        "write"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "input",
    "output",
    "cache"
  ],
  "additionalProperties": false
}
```

<a id="schema-Model.Info"></a>

### Model.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "modelID": {
      "type": "string"
    },
    "providerID": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "canonical": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "family": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "compatibility": {
      "$ref": "#/components/schemas/Model.Compatibility"
    },
    "package": {
      "type": "string"
    },
    "settings": {
      "$ref": "#/components/schemas/Model.Settings"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "body": {
      "type": "object"
    },
    "capabilities": {
      "$ref": "#/components/schemas/Model.Capabilities"
    },
    "variants": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Model.Variant"
      }
    },
    "time": {
      "type": "object",
      "properties": {
        "released": {
          "type": "number"
        }
      },
      "required": [
        "released"
      ],
      "additionalProperties": false
    },
    "cost": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Model.Cost"
      }
    },
    "status": {
      "type": "string",
      "enum": [
        "alpha",
        "beta",
        "deprecated",
        "active"
      ]
    },
    "enabled": {
      "type": "boolean"
    },
    "limit": {
      "type": "object",
      "properties": {
        "context": {
          "type": "integer"
        },
        "input": {
          "type": "integer"
        },
        "output": {
          "type": "integer"
        }
      },
      "required": [
        "context",
        "output"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "id",
    "modelID",
    "providerID",
    "name",
    "capabilities",
    "variants",
    "time",
    "cost",
    "status",
    "enabled",
    "limit"
  ],
  "additionalProperties": false
}
```

<a id="schema-Model.MaxTokensField"></a>

### Model.MaxTokensField

```json
{
  "type": "string",
  "enum": [
    "max_completion_tokens",
    "max_tokens"
  ]
}
```

<a id="schema-Model.ReasoningField"></a>

### Model.ReasoningField

```json
{
  "anyOf": [
    {
      "type": "string",
      "enum": [
        "reasoning",
        "reasoning_content",
        "reasoning_text"
      ]
    },
    {
      "type": "string"
    }
  ]
}
```

<a id="schema-Model.Ref"></a>

### Model.Ref

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "providerID": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "variant": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "providerID"
  ],
  "additionalProperties": false
}
```

<a id="schema-Model.Settings"></a>

### Model.Settings

```json
{
  "type": "object",
  "properties": {
    "compaction": {
      "$ref": "#/components/schemas/Provider.Compaction"
    },
    "encoding": {
      "$ref": "#/components/schemas/Provider.Encoding"
    }
  },
  "allOf": [
    {
      "type": "object",
      "additionalProperties": {}
    }
  ]
}
```

<a id="schema-Model.Variant"></a>

### Model.Variant

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "settings": {
      "$ref": "#/components/schemas/Model.Settings"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "body": {
      "type": "object"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-Money.USD"></a>

### Money.USD

```json
{
  "type": "number"
}
```

<a id="schema-Money.USDPerMillionTokens"></a>

### Money.USDPerMillionTokens

```json
{
  "type": "number"
}
```

<a id="schema-PairingCode"></a>

### PairingCode

```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "string"
    },
    "expires_in": {
      "type": "integer"
    }
  },
  "required": [
    "code",
    "expires_in"
  ],
  "additionalProperties": false
}
```

<a id="schema-PairingSession"></a>

### PairingSession

```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    }
  },
  "required": [
    "token"
  ],
  "additionalProperties": false
}
```

<a id="schema-Permission.Effect"></a>

### Permission.Effect

```json
{
  "type": "string",
  "enum": [
    "allow",
    "deny",
    "ask"
  ]
}
```

<a id="schema-Permission.ID"></a>

### Permission.ID

```json
{
  "type": "string",
  "pattern": "^per"
}
```

<a id="schema-Permission.Reply"></a>

### Permission.Reply

```json
{
  "type": "string",
  "enum": [
    "once",
    "always",
    "reject"
  ]
}
```

<a id="schema-Permission.Request"></a>

### Permission.Request

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Permission.ID"
    },
    "sessionID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "action": {
      "type": "string"
    },
    "resources": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "save": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "metadata": {
      "type": "object"
    },
    "source": {
      "$ref": "#/components/schemas/Permission.Source"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "sessionID",
    "action",
    "resources"
  ],
  "additionalProperties": false
}
```

<a id="schema-Permission.Rule"></a>

### Permission.Rule

```json
{
  "type": "object",
  "properties": {
    "action": {
      "type": "string"
    },
    "resource": {
      "type": "string"
    },
    "effect": {
      "$ref": "#/components/schemas/Permission.Effect"
    }
  },
  "required": [
    "action",
    "resource",
    "effect"
  ],
  "additionalProperties": false
}
```

<a id="schema-Permission.Ruleset"></a>

### Permission.Ruleset

```json
{
  "type": "array",
  "items": {
    "$ref": "#/components/schemas/Permission.Rule"
  }
}
```

<a id="schema-Permission.Source"></a>

### Permission.Source

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "tool"
          ]
        },
        "messageID": {
          "type": "string"
        },
        "id": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "messageID",
        "id"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-PermissionNotFoundErrorEncoded"></a>

### PermissionNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "PermissionNotFoundError"
      ]
    },
    "requestID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "requestID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-PermissionSaved.ID"></a>

### PermissionSaved.ID

```json
{
  "type": "string"
}
```

<a id="schema-PermissionSaved.Info"></a>

### PermissionSaved.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/PermissionSaved.ID"
    },
    "projectID": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "action": {
      "type": "string"
    },
    "resource": {
      "type": "string"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        },
        "updated": {
          "type": "number"
        }
      },
      "required": [
        "created",
        "updated"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "id",
    "projectID",
    "action",
    "resource",
    "time"
  ],
  "additionalProperties": false
}
```

<a id="schema-PersistentPty.CreateInput"></a>

### PersistentPty.CreateInput

```json
{
  "type": "object",
  "properties": {
    "command": {
      "type": "string"
    },
    "args": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "cwd": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "env": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "size": {
      "type": "object",
      "properties": {
        "cols": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "rows": {
          "type": "integer",
          "exclusiveMinimum": 0
        }
      },
      "required": [
        "cols",
        "rows"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "args",
    "title",
    "env"
  ],
  "additionalProperties": false
}
```

<a id="schema-PersistentPty.Handoff"></a>

### PersistentPty.Handoff

```json
{
  "type": "object",
  "properties": {
    "directory": {
      "type": "string"
    },
    "instanceID": {
      "type": "string"
    },
    "ticket": {
      "type": "string"
    },
    "expiresAt": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    }
  },
  "required": [
    "directory",
    "instanceID",
    "ticket",
    "expiresAt"
  ],
  "additionalProperties": false
}
```

<a id="schema-PersistentPty.Info"></a>

### PersistentPty.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Pty.ID"
    },
    "title": {
      "type": "string"
    },
    "command": {
      "type": "string"
    },
    "args": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "cwd": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "exited"
      ]
    },
    "pid": {
      "type": "integer",
      "minimum": 0
    },
    "exitCode": {
      "type": "integer",
      "minimum": 0
    },
    "sessionID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "foregroundProcess": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "size": {
      "type": "object",
      "properties": {
        "cols": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "rows": {
          "type": "integer",
          "exclusiveMinimum": 0
        }
      },
      "required": [
        "cols",
        "rows"
      ],
      "additionalProperties": false
    },
    "output": {
      "type": "object",
      "properties": {
        "head": {
          "type": "integer",
          "minimum": 0
        },
        "tail": {
          "type": "integer",
          "minimum": 0
        }
      },
      "required": [
        "head",
        "tail"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "id",
    "title",
    "command",
    "args",
    "cwd",
    "status",
    "pid",
    "sessionID",
    "foregroundProcess",
    "size",
    "output"
  ],
  "additionalProperties": false
}
```

<a id="schema-PersistentPty.ReadLinesEncoded"></a>

### PersistentPty.ReadLinesEncoded

```json
{
  "type": "string"
}
```

<a id="schema-PersistentPty.ReadResult"></a>

### PersistentPty.ReadResult

```json
{
  "type": "object",
  "properties": {
    "ptyID": {
      "$ref": "#/components/schemas/Pty.ID"
    },
    "title": {
      "type": "string"
    },
    "cwd": {
      "type": "string"
    },
    "foregroundProcess": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    },
    "screen": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string"
        },
        "cols": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "rows": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "cursor": {
          "type": "object",
          "properties": {
            "x": {
              "type": "integer",
              "minimum": 0
            },
            "y": {
              "type": "integer",
              "minimum": 0
            }
          },
          "required": [
            "x",
            "y"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "text",
        "cols",
        "rows",
        "cursor"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "ptyID",
    "title",
    "cwd",
    "foregroundProcess",
    "screen"
  ],
  "additionalProperties": false
}
```

<a id="schema-PersistentPty.Snapshot"></a>

### PersistentPty.Snapshot

```json
{
  "type": "object",
  "properties": {
    "info": {
      "$ref": "#/components/schemas/PersistentPty.Info"
    },
    "text": {
      "type": "string"
    },
    "checkpoint": {
      "type": "string",
      "format": "byte",
      "contentEncoding": "base64"
    },
    "cursor": {
      "type": "object",
      "properties": {
        "x": {
          "type": "integer",
          "minimum": 0
        },
        "y": {
          "type": "integer",
          "minimum": 0
        }
      },
      "required": [
        "x",
        "y"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "info",
    "text",
    "checkpoint",
    "cursor"
  ],
  "additionalProperties": false
}
```

<a id="schema-PersistentPty.UpdateInput"></a>

### PersistentPty.UpdateInput

```json
{
  "type": "object",
  "properties": {
    "attachmentID": {
      "type": "string"
    },
    "size": {
      "type": "object",
      "properties": {
        "cols": {
          "type": "integer",
          "exclusiveMinimum": 0
        },
        "rows": {
          "type": "integer",
          "exclusiveMinimum": 0
        }
      },
      "required": [
        "cols",
        "rows"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "size"
  ],
  "additionalProperties": false
}
```

<a id="schema-Plugin.Features"></a>

### Plugin.Features

```json
{
  "type": "object",
  "properties": {
    "server": {
      "type": "boolean",
      "enum": [
        true
      ]
    },
    "tui": {
      "type": "boolean",
      "enum": [
        true
      ]
    },
    "rpc": {
      "type": "boolean",
      "enum": [
        true
      ]
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Plugin.Info"></a>

### Plugin.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "source": {
      "$ref": "#/components/schemas/Plugin.Source"
    },
    "features": {
      "$ref": "#/components/schemas/Plugin.Features"
    },
    "state": {
      "$ref": "#/components/schemas/Plugin.State"
    }
  },
  "required": [
    "source",
    "features",
    "state"
  ],
  "additionalProperties": false
}
```

<a id="schema-Plugin.Source"></a>

### Plugin.Source

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "builtin"
          ]
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "package"
          ]
        },
        "target": {
          "type": "string"
        },
        "version": {
          "type": "string"
        },
        "outdated": {
          "type": "boolean",
          "enum": [
            true
          ]
        },
        "updating": {
          "type": "boolean",
          "enum": [
            true
          ]
        }
      },
      "required": [
        "type",
        "target"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "local"
          ]
        },
        "path": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "path"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "sdk"
          ]
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Plugin.State"></a>

### Plugin.State

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "active"
          ]
        }
      },
      "required": [
        "status"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "failed"
          ]
        },
        "error": {
          "type": "string"
        },
        "ref": {
          "type": "string"
        }
      },
      "required": [
        "status",
        "error"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Project"></a>

### Project

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "canonical": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "vcs": {
      "$ref": "#/components/schemas/Project.Vcs"
    },
    "name": {
      "type": "string"
    },
    "icon": {
      "$ref": "#/components/schemas/Project.Icon"
    },
    "commands": {
      "$ref": "#/components/schemas/Project.Commands"
    },
    "time": {
      "$ref": "#/components/schemas/Project.Time"
    },
    "sandboxes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "id",
    "canonical",
    "time",
    "sandboxes"
  ],
  "additionalProperties": false
}
```

<a id="schema-Project.Commands"></a>

### Project.Commands

```json
{
  "type": "object",
  "properties": {
    "start": {
      "type": "string",
      "description": "Startup script to run when creating a new workspace (worktree)"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Project.ID"></a>

### Project.ID

```json
{
  "type": "string"
}
```

<a id="schema-Project.Icon"></a>

### Project.Icon

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string"
    },
    "override": {
      "type": "string"
    },
    "color": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Project.Time"></a>

### Project.Time

```json
{
  "type": "object",
  "properties": {
    "created": {
      "type": "integer",
      "minimum": 0
    },
    "updated": {
      "type": "integer",
      "minimum": 0
    },
    "active": {
      "type": "integer",
      "minimum": 0
    },
    "archived": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "created",
    "updated",
    "active"
  ],
  "additionalProperties": false
}
```

<a id="schema-Project.Vcs"></a>

### Project.Vcs

```json
{
  "type": "string",
  "pattern": "^[a-z][a-z0-9._-]*$"
}
```

<a id="schema-ProjectNotFoundErrorEncoded"></a>

### ProjectNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "ProjectNotFoundError"
      ]
    },
    "projectID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "projectID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Prompt.AgentAttachment"></a>

### Prompt.AgentAttachment

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "mention": {
      "$ref": "#/components/schemas/Prompt.Mention"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-Prompt.Base64"></a>

### Prompt.Base64

```json
{
  "type": "string",
  "pattern": "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
}
```

<a id="schema-Prompt.FileAttachment"></a>

### Prompt.FileAttachment

```json
{
  "type": "object",
  "properties": {
    "data": {
      "$ref": "#/components/schemas/Prompt.Base64"
    },
    "mime": {
      "type": "string"
    },
    "source": {
      "$ref": "#/components/schemas/Prompt.FileSource"
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mention": {
      "$ref": "#/components/schemas/Prompt.Mention"
    }
  },
  "required": [
    "data",
    "mime",
    "source"
  ],
  "additionalProperties": false
}
```

<a id="schema-Prompt.FileSource"></a>

### Prompt.FileSource

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "inline"
          ]
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "uri"
          ]
        },
        "uri": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "uri"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Prompt.Mention"></a>

### Prompt.Mention

```json
{
  "type": "object",
  "properties": {
    "start": {
      "type": "number"
    },
    "end": {
      "type": "number"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "start",
    "end",
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Prompt.SkillAttachment"></a>

### Prompt.SkillAttachment

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Skill.ID"
    },
    "name": {
      "$ref": "#/components/schemas/Skill.Name"
    },
    "text": {
      "type": "string"
    },
    "mention": {
      "$ref": "#/components/schemas/Prompt.Mention"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-PromptInput.FileAttachment"></a>

### PromptInput.FileAttachment

```json
{
  "type": "object",
  "properties": {
    "uri": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "mention": {
      "$ref": "#/components/schemas/Prompt.Mention"
    }
  },
  "required": [
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="schema-PromptInput.SkillAttachment"></a>

### PromptInput.SkillAttachment

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Skill.ID"
    },
    "mention": {
      "$ref": "#/components/schemas/Prompt.Mention"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="schema-Provider.Compaction"></a>

### Provider.Compaction

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "summary"
          ]
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "native"
          ]
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Provider.Compatibility"></a>

### Provider.Compatibility

```json
{
  "type": "object",
  "properties": {
    "reasoningField": {
      "$ref": "#/components/schemas/Model.ReasoningField"
    },
    "requireReasoning": {
      "type": "boolean"
    },
    "maxTokensField": {
      "$ref": "#/components/schemas/Model.MaxTokensField"
    },
    "requireFinishReason": {
      "type": "boolean"
    },
    "requireAssistantAfterTool": {
      "type": "boolean"
    },
    "supportsPromptCacheKey": {
      "type": "boolean"
    },
    "cacheFormat": {
      "$ref": "#/components/schemas/Model.CacheFormat"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Provider.Encoding"></a>

### Provider.Encoding

```json
{
  "type": "string",
  "enum": [
    "zstd",
    "gzip",
    "none"
  ]
}
```

<a id="schema-Provider.ID"></a>

### Provider.ID

```json
{
  "type": "string"
}
```

<a id="schema-Provider.Info"></a>

### Provider.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "canonical": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "integrationID": {
      "$ref": "#/components/schemas/Integration.ID"
    },
    "name": {
      "type": "string"
    },
    "activation": {
      "type": "string",
      "enum": [
        "auto",
        "enabled",
        "disabled"
      ]
    },
    "package": {
      "type": "string"
    },
    "compatibility": {
      "$ref": "#/components/schemas/Provider.Compatibility"
    },
    "settings": {
      "$ref": "#/components/schemas/Provider.Settings"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "body": {
      "type": "object"
    }
  },
  "required": [
    "id",
    "name",
    "activation",
    "package"
  ],
  "additionalProperties": false
}
```

<a id="schema-Provider.Request"></a>

### Provider.Request

```json
{
  "type": "object",
  "properties": {
    "settings": {
      "$ref": "#/components/schemas/Provider.Settings"
    },
    "headers": {
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "body": {
      "type": "object"
    }
  },
  "required": [
    "settings",
    "headers",
    "body"
  ],
  "additionalProperties": false
}
```

<a id="schema-Provider.Settings"></a>

### Provider.Settings

```json
{
  "type": "object",
  "properties": {
    "timeout": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "headerTimeout": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "chunkTimeout": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean",
          "enum": [
            false
          ]
        }
      ]
    },
    "compaction": {
      "$ref": "#/components/schemas/Provider.Compaction"
    },
    "transport": {
      "$ref": "#/components/schemas/Provider.Transport"
    },
    "encoding": {
      "$ref": "#/components/schemas/Provider.Encoding"
    }
  },
  "allOf": [
    {
      "type": "object",
      "additionalProperties": {}
    }
  ]
}
```

<a id="schema-Provider.Transport"></a>

### Provider.Transport

```json
{
  "type": "string",
  "enum": [
    "http",
    "websocket"
  ]
}
```

<a id="schema-ProviderNotFoundErrorEncoded"></a>

### ProviderNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "ProviderNotFoundError"
      ]
    },
    "providerID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "providerID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Pty"></a>

### Pty

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Pty.ID"
    },
    "title": {
      "type": "string"
    },
    "command": {
      "type": "string"
    },
    "args": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "cwd": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "exited"
      ]
    },
    "pid": {
      "type": "integer",
      "minimum": 0
    },
    "exitCode": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "id",
    "title",
    "command",
    "args",
    "cwd",
    "status",
    "pid"
  ],
  "additionalProperties": false
}
```

<a id="schema-Pty.ID"></a>

### Pty.ID

```json
{
  "type": "string",
  "pattern": "^pty"
}
```

<a id="schema-PtyNotFoundErrorEncoded"></a>

### PtyNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "PtyNotFoundError"
      ]
    },
    "ptyID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "ptyID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-PtyTicket.ConnectToken"></a>

### PtyTicket.ConnectToken

```json
{
  "type": "object",
  "properties": {
    "ticket": {
      "type": "string"
    },
    "expires_in": {
      "type": "integer",
      "exclusiveMinimum": 0
    }
  },
  "required": [
    "ticket",
    "expires_in"
  ],
  "additionalProperties": false
}
```

<a id="schema-Reference.GitSource"></a>

### Reference.GitSource

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "git"
      ]
    },
    "repository": {
      "type": "string"
    },
    "branch": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "repository"
  ],
  "additionalProperties": false
}
```

<a id="schema-Reference.Info"></a>

### Reference.Info

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "path": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "description": {
      "type": "string"
    },
    "hidden": {
      "type": "boolean"
    },
    "source": {
      "$ref": "#/components/schemas/Reference.Source"
    }
  },
  "required": [
    "name",
    "path",
    "source"
  ],
  "additionalProperties": false
}
```

<a id="schema-Reference.LocalSource"></a>

### Reference.LocalSource

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "local"
      ]
    },
    "path": {
      "$ref": "#/components/schemas/AbsolutePath"
    }
  },
  "required": [
    "type",
    "path"
  ],
  "additionalProperties": false
}
```

<a id="schema-Reference.Source"></a>

### Reference.Source

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Reference.LocalSource"
    },
    {
      "$ref": "#/components/schemas/Reference.GitSource"
    }
  ]
}
```

<a id="schema-RelativePath"></a>

### RelativePath

```json
{
  "type": "string"
}
```

<a id="schema-Rpc.Input"></a>

### Rpc.Input

```json
{
  "type": "object",
  "properties": {
    "input": {}
  },
  "additionalProperties": false
}
```

<a id="schema-Rpc.Output"></a>

### Rpc.Output

```json
{
  "type": "object",
  "properties": {
    "output": {}
  },
  "additionalProperties": false
}
```

<a id="schema-RpcErrorEncoded"></a>

### RpcErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "RpcError"
      ]
    },
    "type": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "anyOf": [
        {},
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "_tag",
    "type",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-RpcInternalErrorEncoded"></a>

### RpcInternalErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "RpcInternalError"
      ]
    },
    "type": {
      "type": "string",
      "enum": [
        "rpc.internal",
        "rpc.invalid_output"
      ]
    },
    "message": {
      "type": "string"
    },
    "data": {
      "anyOf": [
        {},
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "_tag",
    "type",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-ServerInfo"></a>

### ServerInfo

```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string"
    },
    "pid": {
      "type": "integer",
      "minimum": 0
    },
    "urls": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "paths": {
      "type": "object",
      "properties": {
        "tmp": {
          "type": "string"
        }
      },
      "required": [
        "tmp"
      ],
      "additionalProperties": false
    },
    "capabilities": {
      "anyOf": [
        {
          "type": "object",
          "properties": {
            "persistentPty": {
              "anyOf": [
                {
                  "type": "boolean"
                },
                {
                  "type": "null"
                }
              ]
            }
          },
          "additionalProperties": false
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "version",
    "pid",
    "urls",
    "paths"
  ],
  "additionalProperties": false
}
```

<a id="schema-ServiceUnavailableErrorEncoded"></a>

### ServiceUnavailableErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "ServiceUnavailableError"
      ]
    },
    "message": {
      "type": "string"
    },
    "service": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.ForkBoundary"></a>

### Session.ForkBoundary

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "before"
          ]
        },
        "messageID": {
          "$ref": "#/components/schemas/Session.Message.ID"
        }
      },
      "required": [
        "type",
        "messageID"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "through"
          ]
        },
        "messageID": {
          "$ref": "#/components/schemas/Session.Message.ID"
        }
      },
      "required": [
        "type",
        "messageID"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-Session.ID"></a>

### Session.ID

```json
{
  "type": "string",
  "pattern": "^ses"
}
```

<a id="schema-Session.Inbox.Compaction"></a>

### Session.Inbox.Compaction

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "sessionID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "compaction"
      ]
    },
    "payload": {
      "$ref": "#/components/schemas/Session.Inbox.CompactionPayload"
    },
    "delivery": {
      "$ref": "#/components/schemas/Session.Inbox.Delivery"
    }
  },
  "required": [
    "id",
    "sessionID",
    "time",
    "type",
    "payload",
    "delivery"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Inbox.CompactionPayload"></a>

### Session.Inbox.CompactionPayload

```json
{
  "not": {
    "type": "null"
  }
}
```

<a id="schema-Session.Inbox.Delivery"></a>

### Session.Inbox.Delivery

```json
{
  "type": "string",
  "enum": [
    "steer",
    "queue"
  ]
}
```

<a id="schema-Session.Inbox.Info"></a>

### Session.Inbox.Info

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Session.Inbox.User"
    },
    {
      "$ref": "#/components/schemas/Session.Inbox.Synthetic"
    },
    {
      "$ref": "#/components/schemas/Session.Inbox.Compaction"
    },
    {
      "$ref": "#/components/schemas/Session.Inbox.Move"
    }
  ]
}
```

<a id="schema-Session.Inbox.Move"></a>

### Session.Inbox.Move

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "sessionID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "move"
      ]
    },
    "delivery": {
      "$ref": "#/components/schemas/Session.Inbox.Delivery"
    },
    "payload": {
      "$ref": "#/components/schemas/Session.Inbox.MovePayload"
    }
  },
  "required": [
    "id",
    "sessionID",
    "time",
    "type",
    "delivery",
    "payload"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Inbox.MovePayload"></a>

### Session.Inbox.MovePayload

```json
{
  "type": "object",
  "properties": {
    "projectID": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "subpath": {
      "$ref": "#/components/schemas/RelativePath"
    },
    "location": {
      "$ref": "#/components/schemas/Location.PublicRef"
    }
  },
  "required": [
    "projectID",
    "location"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Inbox.Synthetic"></a>

### Session.Inbox.Synthetic

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "sessionID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "synthetic"
      ]
    },
    "payload": {
      "$ref": "#/components/schemas/Session.Inbox.SyntheticPayload"
    },
    "delivery": {
      "$ref": "#/components/schemas/Session.Inbox.Delivery"
    }
  },
  "required": [
    "id",
    "sessionID",
    "time",
    "type",
    "payload",
    "delivery"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Inbox.SyntheticPayload"></a>

### Session.Inbox.SyntheticPayload

```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Inbox.User"></a>

### Session.Inbox.User

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "sessionID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "user"
      ]
    },
    "payload": {
      "$ref": "#/components/schemas/Session.Inbox.UserPayload"
    },
    "delivery": {
      "$ref": "#/components/schemas/Session.Inbox.Delivery"
    }
  },
  "required": [
    "id",
    "sessionID",
    "time",
    "type",
    "payload",
    "delivery"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Inbox.UserPayload"></a>

### Session.Inbox.UserPayload

```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    },
    "files": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Prompt.FileAttachment"
      }
    },
    "agents": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Prompt.AgentAttachment"
      }
    },
    "skills": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Prompt.SkillAttachment"
      }
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Info"></a>

### Session.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "parentID": {
      "$ref": "#/components/schemas/Session.ID"
    },
    "fork": {
      "type": "object",
      "properties": {
        "sessionID": {
          "$ref": "#/components/schemas/Session.ID"
        },
        "boundary": {
          "$ref": "#/components/schemas/Session.ForkBoundary"
        }
      },
      "required": [
        "sessionID",
        "boundary"
      ],
      "additionalProperties": false
    },
    "projectID": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "agent": {
      "$ref": "#/components/schemas/Agent.ID"
    },
    "model": {
      "$ref": "#/components/schemas/Model.Ref"
    },
    "cost": {
      "$ref": "#/components/schemas/Money.USD"
    },
    "tokens": {
      "$ref": "#/components/schemas/TokenUsage.Info"
    },
    "outcome": {
      "type": "string",
      "enum": [
        "succeeded",
        "failed",
        "interrupted"
      ]
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        },
        "updated": {
          "type": "number"
        },
        "idle": {
          "type": "number"
        },
        "viewed": {
          "type": "number"
        },
        "archived": {
          "type": "number"
        }
      },
      "required": [
        "created",
        "updated"
      ],
      "additionalProperties": false
    },
    "title": {
      "type": "string"
    },
    "subpath": {
      "$ref": "#/components/schemas/RelativePath"
    },
    "metadata": {
      "$ref": "#/components/schemas/Session.Metadata"
    },
    "permissions": {
      "$ref": "#/components/schemas/Permission.Ruleset"
    },
    "revert": {
      "$ref": "#/components/schemas/Session.Revert"
    },
    "location": {
      "$ref": "#/components/schemas/Location.PublicRef"
    }
  },
  "required": [
    "id",
    "projectID",
    "cost",
    "tokens",
    "time",
    "location"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.AgentSelected"></a>

### Session.Message.AgentSelected

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "agent-switched"
      ]
    },
    "agent": {
      "$ref": "#/components/schemas/Agent.ID"
    },
    "previous": {
      "$ref": "#/components/schemas/Agent.ID"
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "agent"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Assistant"></a>

### Session.Message.Assistant

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        },
        "streamed": {
          "type": "number"
        },
        "completed": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "assistant"
      ]
    },
    "agent": {
      "$ref": "#/components/schemas/Agent.ID"
    },
    "model": {
      "$ref": "#/components/schemas/Model.Ref"
    },
    "content": {
      "type": "array",
      "items": {
        "anyOf": [
          {
            "$ref": "#/components/schemas/Session.Message.Assistant.Text"
          },
          {
            "$ref": "#/components/schemas/Session.Message.Assistant.Reasoning"
          },
          {
            "$ref": "#/components/schemas/Session.Message.Assistant.Tool"
          }
        ]
      }
    },
    "snapshot": {
      "type": "object",
      "properties": {
        "start": {
          "$ref": "#/components/schemas/Snapshot.ID"
        },
        "end": {
          "$ref": "#/components/schemas/Snapshot.ID"
        },
        "files": {
          "type": "array",
          "items": {
            "$ref": "#/components/schemas/RelativePath"
          }
        }
      },
      "additionalProperties": false
    },
    "finish": {
      "type": "string",
      "enum": [
        "stop",
        "length",
        "tool-calls",
        "content-filter",
        "error",
        "unknown"
      ]
    },
    "rawFinish": {
      "type": "string"
    },
    "providerState": {
      "$ref": "#/components/schemas/Session.Message.ProviderState_4"
    },
    "cost": {
      "$ref": "#/components/schemas/Money.USD"
    },
    "tokens": {
      "$ref": "#/components/schemas/TokenUsage.Info"
    },
    "error": {
      "$ref": "#/components/schemas/Session.StructuredError"
    },
    "retry": {
      "$ref": "#/components/schemas/Session.Message.Assistant.Retry"
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "agent",
    "model",
    "content"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Assistant.Reasoning"></a>

### Session.Message.Assistant.Reasoning

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "reasoning"
      ]
    },
    "text": {
      "type": "string"
    },
    "state": {
      "$ref": "#/components/schemas/Session.Message.ProviderState_1"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        },
        "completed": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "type",
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Assistant.Retry"></a>

### Session.Message.Assistant.Retry

```json
{
  "type": "object",
  "properties": {
    "attempt": {
      "type": "integer",
      "exclusiveMinimum": 0
    },
    "at": {
      "type": "number"
    },
    "error": {
      "$ref": "#/components/schemas/Session.StructuredError"
    }
  },
  "required": [
    "attempt",
    "at",
    "error"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Assistant.Text"></a>

### Session.Message.Assistant.Text

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "text"
      ]
    },
    "text": {
      "type": "string"
    },
    "state": {
      "$ref": "#/components/schemas/Session.Message.ProviderState"
    }
  },
  "required": [
    "type",
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Assistant.Tool"></a>

### Session.Message.Assistant.Tool

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "tool"
      ]
    },
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "executed": {
      "type": "boolean"
    },
    "providerState": {
      "$ref": "#/components/schemas/Session.Message.ProviderState_2"
    },
    "providerResultState": {
      "$ref": "#/components/schemas/Session.Message.ProviderState_3"
    },
    "state": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/Session.Message.ToolState.Streaming"
        },
        {
          "$ref": "#/components/schemas/Session.Message.ToolState.Running"
        },
        {
          "$ref": "#/components/schemas/Session.Message.ToolState.Completed"
        },
        {
          "$ref": "#/components/schemas/Session.Message.ToolState.Error"
        }
      ]
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        },
        "ran": {
          "type": "number"
        },
        "completed": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "type",
    "id",
    "name",
    "state",
    "time"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Compaction"></a>

### Session.Message.Compaction

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Session.Message.Compaction.Running"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Compaction.Completed"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Compaction.Failed"
    }
  ]
}
```

<a id="schema-Session.Message.Compaction.Completed"></a>

### Session.Message.Compaction.Completed

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "compaction"
      ]
    },
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "status": {
      "type": "string",
      "enum": [
        "completed"
      ]
    },
    "reason": {
      "type": "string",
      "enum": [
        "auto",
        "manual"
      ]
    },
    "model": {
      "$ref": "#/components/schemas/Model.Ref"
    },
    "providerState": {
      "$ref": "#/components/schemas/Session.Message.ProviderState_5"
    },
    "summary": {
      "type": "string"
    },
    "recent": {
      "type": "string"
    },
    "providerContext": {
      "$ref": "#/components/schemas/Session.ProviderContext"
    },
    "cost": {
      "$ref": "#/components/schemas/Money.USD"
    },
    "tokens": {
      "$ref": "#/components/schemas/TokenUsage.Info"
    }
  },
  "required": [
    "type",
    "id",
    "time",
    "status",
    "reason",
    "summary",
    "recent"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Compaction.Failed"></a>

### Session.Message.Compaction.Failed

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "compaction"
      ]
    },
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "status": {
      "type": "string",
      "enum": [
        "failed"
      ]
    },
    "reason": {
      "type": "string",
      "enum": [
        "auto",
        "manual"
      ]
    },
    "error": {
      "$ref": "#/components/schemas/Session.StructuredError"
    },
    "cost": {
      "$ref": "#/components/schemas/Money.USD"
    },
    "tokens": {
      "$ref": "#/components/schemas/TokenUsage.Info"
    }
  },
  "required": [
    "type",
    "id",
    "time",
    "status",
    "reason",
    "error"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Compaction.Running"></a>

### Session.Message.Compaction.Running

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "compaction"
      ]
    },
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "status": {
      "type": "string",
      "enum": [
        "running"
      ]
    },
    "reason": {
      "type": "string",
      "enum": [
        "auto",
        "manual"
      ]
    },
    "summary": {
      "type": "string"
    },
    "recent": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "id",
    "time",
    "status",
    "reason",
    "summary",
    "recent"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ID"></a>

### Session.Message.ID

```json
{
  "type": "string",
  "pattern": "^msg_"
}
```

<a id="schema-Session.Message.Idle"></a>

### Session.Message.Idle

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "idle"
      ]
    },
    "outcome": {
      "type": "string",
      "enum": [
        "succeeded",
        "failed",
        "interrupted"
      ]
    },
    "error": {
      "$ref": "#/components/schemas/Session.StructuredError"
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "outcome"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Info"></a>

### Session.Message.Info

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Session.Message.AgentSelected"
    },
    {
      "$ref": "#/components/schemas/Session.Message.ModelSelected"
    },
    {
      "$ref": "#/components/schemas/Session.Message.LocationSwitched"
    },
    {
      "$ref": "#/components/schemas/Session.Message.User"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Synthetic"
    },
    {
      "$ref": "#/components/schemas/Session.Message.System"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Skill"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Shell"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Assistant"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Compaction"
    },
    {
      "$ref": "#/components/schemas/Session.Message.Idle"
    }
  ]
}
```

<a id="schema-Session.Message.LocationSwitched"></a>

### Session.Message.LocationSwitched

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "location-switched"
      ]
    },
    "projectID": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "subpath": {
      "$ref": "#/components/schemas/RelativePath"
    },
    "location": {
      "$ref": "#/components/schemas/Location.PublicRef"
    },
    "previous": {
      "anyOf": [
        {
          "type": "object",
          "properties": {
            "location": {
              "$ref": "#/components/schemas/Location.PublicRef"
            },
            "projectID": {
              "$ref": "#/components/schemas/Project.ID"
            },
            "subpath": {
              "$ref": "#/components/schemas/RelativePath"
            }
          },
          "required": [
            "location"
          ],
          "additionalProperties": false
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "location"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ModelSelected"></a>

### Session.Message.ModelSelected

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "model-switched"
      ]
    },
    "model": {
      "$ref": "#/components/schemas/Model.Ref"
    },
    "previous": {
      "$ref": "#/components/schemas/Model.Ref"
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "model"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ProviderState"></a>

### Session.Message.ProviderState

```json
{
  "type": "object"
}
```

<a id="schema-Session.Message.ProviderState_1"></a>

### Session.Message.ProviderState_1

```json
{
  "type": "object"
}
```

<a id="schema-Session.Message.ProviderState_2"></a>

### Session.Message.ProviderState_2

```json
{
  "type": "object"
}
```

<a id="schema-Session.Message.ProviderState_3"></a>

### Session.Message.ProviderState_3

```json
{
  "type": "object"
}
```

<a id="schema-Session.Message.ProviderState_4"></a>

### Session.Message.ProviderState_4

```json
{
  "type": "object"
}
```

<a id="schema-Session.Message.ProviderState_5"></a>

### Session.Message.ProviderState_5

```json
{
  "type": "object"
}
```

<a id="schema-Session.Message.Shell"></a>

### Session.Message.Shell

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        },
        "completed": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "shell"
      ]
    },
    "shellID": {
      "$ref": "#/components/schemas/Shell.ID"
    },
    "command": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "exited",
        "timeout",
        "killed"
      ]
    },
    "exit": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "string",
          "enum": [
            "Infinity",
            "-Infinity",
            "NaN"
          ]
        }
      ]
    },
    "output": {
      "type": "object",
      "properties": {
        "output": {
          "type": "string"
        },
        "cursor": {
          "type": "integer",
          "minimum": 0
        },
        "size": {
          "type": "integer",
          "minimum": 0
        },
        "truncated": {
          "type": "boolean"
        }
      },
      "required": [
        "output",
        "cursor",
        "size",
        "truncated"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "shellID",
    "command",
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Skill"></a>

### Session.Message.Skill

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "skill"
      ]
    },
    "skill": {
      "$ref": "#/components/schemas/Skill.ID"
    },
    "name": {
      "$ref": "#/components/schemas/Skill.Name"
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "skill",
    "name",
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.Synthetic"></a>

### Session.Message.Synthetic

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "text": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "type": {
      "type": "string",
      "enum": [
        "synthetic"
      ]
    }
  },
  "required": [
    "id",
    "time",
    "text",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.System"></a>

### Session.Message.System

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "type": {
      "type": "string",
      "enum": [
        "system"
      ]
    },
    "text": {
      "type": "string"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "time",
    "type",
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ToolState.Completed"></a>

### Session.Message.ToolState.Completed

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "completed"
      ]
    },
    "input": {
      "type": "object"
    },
    "content": {
      "type": "array",
      "prefixItems": [
        {
          "$ref": "#/components/schemas/Tool.Content"
        }
      ],
      "minItems": 1,
      "items": {
        "$ref": "#/components/schemas/Tool.Content"
      }
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "status",
    "input",
    "content"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ToolState.Error"></a>

### Session.Message.ToolState.Error

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "error"
      ]
    },
    "input": {
      "type": "object"
    },
    "error": {
      "$ref": "#/components/schemas/Session.StructuredError"
    },
    "content": {
      "type": "array",
      "prefixItems": [
        {
          "$ref": "#/components/schemas/Tool.Content"
        }
      ],
      "minItems": 1,
      "items": {
        "$ref": "#/components/schemas/Tool.Content"
      }
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "status",
    "input",
    "error"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ToolState.Running"></a>

### Session.Message.ToolState.Running

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "running"
      ]
    },
    "input": {
      "type": "object"
    },
    "metadata": {
      "type": "object"
    }
  },
  "required": [
    "status",
    "input",
    "metadata"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.ToolState.Streaming"></a>

### Session.Message.ToolState.Streaming

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": [
        "streaming"
      ]
    },
    "input": {
      "type": "string"
    }
  },
  "required": [
    "status",
    "input"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Message.User"></a>

### Session.Message.User

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "created": {
          "type": "number"
        }
      },
      "required": [
        "created"
      ],
      "additionalProperties": false
    },
    "text": {
      "type": "string"
    },
    "files": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Prompt.FileAttachment"
      }
    },
    "agents": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Prompt.AgentAttachment"
      }
    },
    "skills": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Prompt.SkillAttachment"
      }
    },
    "type": {
      "type": "string",
      "enum": [
        "user"
      ]
    }
  },
  "required": [
    "id",
    "time",
    "text",
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Metadata"></a>

### Session.Metadata

```json
{
  "type": "object"
}
```

<a id="schema-Session.ProviderContext"></a>

### Session.ProviderContext

```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number",
      "enum": [
        1
      ]
    },
    "provenance": {
      "$ref": "#/components/schemas/Session.ProviderContext.Provenance"
    },
    "messages": {}
  },
  "required": [
    "version",
    "provenance",
    "messages"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.ProviderContext.Provenance"></a>

### Session.ProviderContext.Provenance

```json
{
  "type": "object",
  "properties": {
    "providerID": {
      "$ref": "#/components/schemas/Provider.ID"
    },
    "provider": {
      "type": "string"
    },
    "modelID": {
      "type": "string"
    },
    "route": {
      "type": "string"
    },
    "protocol": {
      "type": "string"
    },
    "endpoint": {
      "type": "string"
    }
  },
  "required": [
    "providerID",
    "provider",
    "modelID",
    "route",
    "protocol",
    "endpoint"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.Revert"></a>

### Session.Revert

```json
{
  "type": "object",
  "properties": {
    "messageID": {
      "$ref": "#/components/schemas/Session.Message.ID"
    },
    "partID": {
      "type": "string"
    },
    "snapshot": {
      "$ref": "#/components/schemas/Snapshot.ID"
    },
    "files": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/FileDiff.Info"
      }
    }
  },
  "required": [
    "messageID"
  ],
  "additionalProperties": false
}
```

<a id="schema-Session.StructuredError"></a>

### Session.StructuredError

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "status": {
      "type": "integer",
      "minimum": 100,
      "maximum": 599
    },
    "response": {
      "type": "object",
      "properties": {
        "body": {
          "type": "string"
        }
      },
      "required": [
        "body"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "type",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionActive"></a>

### SessionActive

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "running"
      ]
    }
  },
  "required": [
    "type"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionBusyErrorEncoded"></a>

### SessionBusyErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "SessionBusyError"
      ]
    },
    "sessionID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "sessionID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionGenerateResponse"></a>

### SessionGenerateResponse

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string"
        }
      },
      "required": [
        "text"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "data"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionInterruptResponse"></a>

### SessionInterruptResponse

```json
{
  "type": "object",
  "properties": {
    "interrupted": {
      "type": "boolean",
      "description": "Whether an active execution owned by this OpenCode process was interrupted."
    }
  },
  "required": [
    "interrupted"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionLogItemEncoded"></a>

### SessionLogItemEncoded

```json
{
  "type": "string",
  "contentMediaType": "application/json"
}
```

<a id="schema-SessionMessagesResponse"></a>

### SessionMessagesResponse

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Session.Message.Info"
      }
    },
    "cursor": {
      "type": "object",
      "properties": {
        "previous": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        },
        "next": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ]
        }
      },
      "additionalProperties": false
    }
  },
  "required": [
    "data",
    "cursor"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionNotFoundErrorEncoded"></a>

### SessionNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "SessionNotFoundError"
      ]
    },
    "sessionID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "sessionID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionStats.Activity"></a>

### SessionStats.Activity

```json
{
  "type": "object",
  "properties": {
    "date": {
      "type": "string"
    },
    "steps": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "date",
    "steps"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionStats.Info"></a>

### SessionStats.Info

```json
{
  "type": "object",
  "properties": {
    "range": {
      "type": "object",
      "properties": {
        "from": {
          "type": "number"
        },
        "to": {
          "type": "number"
        }
      },
      "required": [
        "from",
        "to"
      ],
      "additionalProperties": false
    },
    "sessions": {
      "type": "integer",
      "minimum": 0
    },
    "subagents": {
      "type": "integer",
      "minimum": 0
    },
    "prompts": {
      "type": "integer",
      "minimum": 0
    },
    "steps": {
      "type": "integer",
      "minimum": 0
    },
    "tokens": {
      "$ref": "#/components/schemas/TokenUsage.Info"
    },
    "cost": {
      "$ref": "#/components/schemas/Money.USD"
    },
    "tools": {
      "$ref": "#/components/schemas/SessionStats.Tools"
    },
    "activeDays": {
      "type": "integer",
      "minimum": 0
    },
    "streak": {
      "type": "integer",
      "minimum": 0
    },
    "activity": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/SessionStats.Activity"
      }
    },
    "models": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/SessionStats.ModelUsage"
      }
    }
  },
  "required": [
    "range",
    "sessions",
    "subagents",
    "prompts",
    "steps",
    "tokens",
    "cost",
    "tools",
    "activeDays",
    "streak",
    "activity",
    "models"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionStats.ModelUsage"></a>

### SessionStats.ModelUsage

```json
{
  "type": "object",
  "properties": {
    "model": {
      "$ref": "#/components/schemas/Model.Ref"
    },
    "steps": {
      "type": "integer",
      "minimum": 0
    },
    "tokens": {
      "$ref": "#/components/schemas/TokenUsage.Info"
    },
    "cost": {
      "$ref": "#/components/schemas/Money.USD"
    }
  },
  "required": [
    "model",
    "steps",
    "tokens",
    "cost"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionStats.ToolTotals"></a>

### SessionStats.ToolTotals

```json
{
  "type": "object",
  "properties": {
    "calls": {
      "type": "integer",
      "minimum": 0
    },
    "succeeded": {
      "type": "integer",
      "minimum": 0
    },
    "failed": {
      "type": "integer",
      "minimum": 0
    },
    "unfinished": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "calls",
    "succeeded",
    "failed",
    "unfinished"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionStats.ToolUsage"></a>

### SessionStats.ToolUsage

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "calls": {
      "type": "integer",
      "minimum": 0
    },
    "succeeded": {
      "type": "integer",
      "minimum": 0
    },
    "failed": {
      "type": "integer",
      "minimum": 0
    },
    "unfinished": {
      "type": "integer",
      "minimum": 0
    },
    "durationP50": {
      "type": "number"
    }
  },
  "required": [
    "name",
    "calls",
    "succeeded",
    "failed",
    "unfinished"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionStats.Tools"></a>

### SessionStats.Tools

```json
{
  "anyOf": [
    {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "none"
          ]
        }
      },
      "required": [
        "mode"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "summary"
          ]
        },
        "totals": {
          "$ref": "#/components/schemas/SessionStats.ToolTotals"
        }
      },
      "required": [
        "mode",
        "totals"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "detail"
          ]
        },
        "totals": {
          "$ref": "#/components/schemas/SessionStats.ToolTotals"
        },
        "usage": {
          "type": "array",
          "items": {
            "$ref": "#/components/schemas/SessionStats.ToolUsage"
          }
        }
      },
      "required": [
        "mode",
        "totals",
        "usage"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="schema-SessionTransfer.Data"></a>

### SessionTransfer.Data

```json
{
  "type": "object",
  "properties": {
    "info": {
      "$ref": "#/components/schemas/Session.Info"
    },
    "messages": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Session.Message.Info"
      }
    }
  },
  "required": [
    "info",
    "messages"
  ],
  "additionalProperties": false
}
```

<a id="schema-SessionsCursor"></a>

### SessionsCursor

```json
{
  "type": "string",
  "description": "Opaque pagination cursor returned as cursor.previous or cursor.next in the previous response."
}
```

<a id="schema-SessionsResponse"></a>

### SessionsResponse

```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Session.Info"
      }
    },
    "cursor": {
      "type": "object",
      "properties": {
        "previous": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/SessionsCursor"
            },
            {
              "type": "null"
            }
          ]
        },
        "next": {
          "anyOf": [
            {
              "$ref": "#/components/schemas/SessionsCursor"
            },
            {
              "type": "null"
            }
          ]
        }
      },
      "additionalProperties": false
    }
  },
  "required": [
    "data",
    "cursor"
  ],
  "additionalProperties": false
}
```

<a id="schema-Shell.ID"></a>

### Shell.ID

```json
{
  "type": "string",
  "pattern": "^sh_"
}
```

<a id="schema-Shell.Info"></a>

### Shell.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Shell.ID"
    },
    "status": {
      "type": "string",
      "enum": [
        "running",
        "exited",
        "timeout",
        "killed"
      ]
    },
    "command": {
      "type": "string"
    },
    "cwd": {
      "type": "string"
    },
    "shell": {
      "type": "string"
    },
    "file": {
      "type": "string"
    },
    "pid": {
      "type": "integer",
      "minimum": 0
    },
    "exit": {
      "type": "number"
    },
    "signal": {
      "type": "string"
    },
    "metadata": {
      "type": "object"
    },
    "time": {
      "type": "object",
      "properties": {
        "started": {
          "type": "number",
          "description": "Start time in milliseconds since the Unix epoch"
        },
        "completed": {
          "type": "number"
        }
      },
      "required": [
        "started"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "id",
    "status",
    "command",
    "cwd",
    "shell",
    "file",
    "metadata",
    "time"
  ],
  "additionalProperties": false
}
```

<a id="schema-ShellNotFoundErrorEncoded"></a>

### ShellNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "ShellNotFoundError"
      ]
    },
    "id": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "id",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Skill.ID"></a>

### Skill.ID

```json
{
  "type": "string"
}
```

<a id="schema-Skill.Info"></a>

### Skill.Info

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/Skill.ID"
    },
    "name": {
      "$ref": "#/components/schemas/Skill.Name"
    },
    "description": {
      "type": "string"
    },
    "autoinvoke": {
      "type": "boolean"
    },
    "path": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "content": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "path",
    "content"
  ],
  "additionalProperties": false
}
```

<a id="schema-Skill.Name"></a>

### Skill.Name

```json
{
  "type": "string"
}
```

<a id="schema-SkillNotFoundErrorEncoded"></a>

### SkillNotFoundErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "SkillNotFoundError"
      ]
    },
    "skill": {
      "$ref": "#/components/schemas/Skill.ID"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "skill",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-Snapshot.ID"></a>

### Snapshot.ID

```json
{
  "type": "string"
}
```

<a id="schema-TokenUsage.Info"></a>

### TokenUsage.Info

```json
{
  "type": "object",
  "properties": {
    "input": {
      "type": "number"
    },
    "output": {
      "type": "number"
    },
    "reasoning": {
      "type": "number"
    },
    "cache": {
      "type": "object",
      "properties": {
        "read": {
          "type": "number"
        },
        "write": {
          "type": "number"
        }
      },
      "required": [
        "read",
        "write"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "input",
    "output",
    "reasoning",
    "cache"
  ],
  "additionalProperties": false
}
```

<a id="schema-Tool.Content"></a>

### Tool.Content

```json
{
  "anyOf": [
    {
      "$ref": "#/components/schemas/Tool.TextContent"
    },
    {
      "$ref": "#/components/schemas/Tool.FileContent"
    }
  ]
}
```

<a id="schema-Tool.FileContent"></a>

### Tool.FileContent

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "file"
      ]
    },
    "uri": {
      "type": "string"
    },
    "mime": {
      "type": "string"
    },
    "name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "type",
    "uri",
    "mime"
  ],
  "additionalProperties": false
}
```

<a id="schema-Tool.TextContent"></a>

### Tool.TextContent

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "text"
      ]
    },
    "text": {
      "type": "string"
    }
  },
  "required": [
    "type",
    "text"
  ],
  "additionalProperties": false
}
```

<a id="schema-UnauthorizedErrorEncoded"></a>

### UnauthorizedErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "UnauthorizedError"
      ]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-UnknownErrorEncoded"></a>

### UnknownErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "UnknownError"
      ]
    },
    "message": {
      "type": "string"
    },
    "ref": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "_tag",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-V2EventEncoded"></a>

### V2EventEncoded

```json
{
  "type": "string",
  "contentMediaType": "application/json"
}
```

<a id="schema-Vcs.Base"></a>

### Vcs.Base

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "ref": {
      "type": "string"
    },
    "source": {
      "type": "string",
      "enum": [
        "reflog",
        "default"
      ]
    }
  },
  "required": [
    "name",
    "ref",
    "source"
  ],
  "additionalProperties": false
}
```

<a id="schema-Vcs.Branch"></a>

### Vcs.Branch

```json
{
  "type": "object",
  "properties": {
    "current": {
      "type": "string"
    },
    "default": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

<a id="schema-Vcs.BranchList"></a>

### Vcs.BranchList

```json
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

<a id="schema-Vcs.FileStatus"></a>

### Vcs.FileStatus

```json
{
  "type": "object",
  "properties": {
    "file": {
      "type": "string"
    },
    "additions": {
      "type": "integer",
      "minimum": 0
    },
    "deletions": {
      "type": "integer",
      "minimum": 0
    },
    "status": {
      "type": "string",
      "enum": [
        "added",
        "deleted",
        "modified"
      ]
    }
  },
  "required": [
    "file",
    "additions",
    "deletions",
    "status"
  ],
  "additionalProperties": false
}
```

<a id="schema-Vcs.Info"></a>

### Vcs.Info

```json
{
  "type": "object",
  "properties": {
    "provider": {
      "type": "string"
    },
    "branch": {
      "$ref": "#/components/schemas/Vcs.Branch"
    }
  },
  "required": [
    "branch"
  ],
  "additionalProperties": false
}
```

<a id="schema-Vcs.Mode"></a>

### Vcs.Mode

```json
{
  "type": "string",
  "enum": [
    "working",
    "branch",
    "committed"
  ]
}
```

<a id="schema-VcsInitNotSupportedErrorEncoded"></a>

### VcsInitNotSupportedErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "VcsInitNotSupportedError"
      ]
    },
    "providerID": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "_tag",
    "providerID",
    "message"
  ],
  "additionalProperties": false
}
```

<a id="schema-WebSearch.ID"></a>

### WebSearch.ID

```json
{
  "type": "string"
}
```

<a id="schema-WebSearch.Provider"></a>

### WebSearch.Provider

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/components/schemas/WebSearch.ID"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="schema-WebSearch.ResponseEncoded"></a>

### WebSearch.ResponseEncoded

```json
{
  "type": "object",
  "properties": {
    "providerID": {
      "$ref": "#/components/schemas/WebSearch.ID"
    },
    "results": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/WebSearch.Result"
      }
    }
  },
  "required": [
    "providerID",
    "results"
  ],
  "additionalProperties": false
}
```

<a id="schema-WebSearch.Result"></a>

### WebSearch.Result

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "content": {
      "type": "string"
    },
    "time": {
      "type": "object",
      "properties": {
        "published": {
          "type": "number"
        }
      },
      "additionalProperties": false
    }
  },
  "required": [
    "url",
    "time"
  ],
  "additionalProperties": false
}
```

<a id="schema-Worktree.CreateInput"></a>

### Worktree.CreateInput

```json
{
  "type": "object",
  "properties": {
    "projectID": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "from": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "branch": {
      "type": "string"
    },
    "directory": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "projectID"
  ],
  "additionalProperties": false
}
```

<a id="schema-Worktree.Directory"></a>

### Worktree.Directory

```json
{
  "type": "object",
  "properties": {
    "directory": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "strategy": {
      "type": "string"
    }
  },
  "required": [
    "directory"
  ],
  "additionalProperties": false
}
```

<a id="schema-Worktree.Info"></a>

### Worktree.Info

```json
{
  "type": "object",
  "properties": {
    "directory": {
      "$ref": "#/components/schemas/AbsolutePath"
    }
  },
  "required": [
    "directory"
  ],
  "additionalProperties": false
}
```

<a id="schema-Worktree.List"></a>

### Worktree.List

```json
{
  "type": "array",
  "items": {
    "$ref": "#/components/schemas/Worktree.Directory"
  }
}
```

<a id="schema-Worktree.RemoveInput"></a>

### Worktree.RemoveInput

```json
{
  "type": "object",
  "properties": {
    "projectID": {
      "$ref": "#/components/schemas/Project.ID"
    },
    "directory": {
      "$ref": "#/components/schemas/AbsolutePath"
    },
    "force": {
      "type": "boolean"
    }
  },
  "required": [
    "projectID",
    "directory",
    "force"
  ],
  "additionalProperties": false
}
```

<a id="schema-WorktreeErrorEncoded"></a>

### WorktreeErrorEncoded

```json
{
  "type": "object",
  "properties": {
    "_tag": {
      "type": "string",
      "enum": [
        "WorktreeError"
      ]
    },
    "name": {
      "type": "string",
      "enum": [
        "WorktreeError"
      ]
    },
    "data": {
      "type": "object",
      "properties": {
        "message": {
          "type": "string"
        },
        "forceRequired": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ]
        }
      },
      "required": [
        "message"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "_tag",
    "name",
    "data"
  ],
  "additionalProperties": false
}
```

## Components: securitySchemes
