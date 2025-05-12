# Getting Started

### Running service:
Run this cmd at ``grammar/``:
```bash
docker build -t grammar-service .
```
And using with any port ``?``:
```bash
docker run -p 3050:? -t grammar-service
```
Make connection to service through ``HTTP POST`` to ``localhost:?/api/grammar/check`` with data in body.
Example:
#### Correct function
* Request body:
```text
{
    function = "(sqrt(x^2 - 1)) / (x - 1)"
}
```
* Response body:
```text
{
    "function": "(sqrt(x**2-1))/(x-1)",
    "errors": null,
    "valid": true
}
```
#### Invalid function
* Request body:
```text
{
    "function": "(sqrt(x^2 - 1)) ( / (x - 1)"
}
```
* Response body:
```text
{
    "function": null,
    "errors": [
        {
            "message": "Syntax error at 17 in input: (sqrt(x**2 - 1)) ( / (x - 1) - mismatched input '(' expecting {'+', '-', '*', '/', '**', ')'}",
            "offendingSymbol": "("
        }
    ],
    "valid": false
}
```