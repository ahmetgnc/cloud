import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    operation = req.params.get('operation')
    number1 = req.params.get('number1')
    number2 = req.params.get('number2')
    if not operation:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            operation = req_body.get('operation')


    def calc(op, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        if op == "sum":
            result = num1 + num2
            return result
        elif op == "mul":
            result = num1 * num2
            return result

    res = calc(operation,number1, number2)

    if res:
        return func.HttpResponse(f"Operation: {operation}  num1: {number1} num2: {number2} Calculation Result  = {res}         Ahmet Genç 115200056")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
