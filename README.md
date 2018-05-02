# furigana_api

## Description
This is a web service to convert a multibyte text into the furigana text.

## Example
```
$ curl -X GET http://localhost:8000/furigana?q=私の名前は太郎です
{"text": "私の名前は太郎です", "furigana": "ワタシノナマエハタロウデス"}
```
