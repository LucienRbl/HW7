## Launch both server 
```bash
python payment_server.py
python card_server.py
```

Payment run on port 50051 and card run on port 50080

### 4est the app  
#### List services
```bash
grpcurl -plaintext localhost:50051 list
```
=>
```
grpc.reflection.v1alpha.ServerReflection
payment.PaymentService
```
#### Add Payment
```bash
grpcurl -plaintext -d '{                                            
    "creditCardNumber": "1234-1234-1234-1234",
    "creditCardOwner": "CardOwner",
    "orderId": "order123"
}' localhost:50051 payment.PaymentService/AddPayment
```
=>
```
{
  "status": "Payment Added"
}
```

#### List Payment
```bash
grpcurl -plaintext localhost:50051 payment.PaymentService/ListPayments
```
=>
```
{
  "payments": [
    {
      "creditCardNumber": "1234-1234-1234-1234",
      "creditCardOwner": "CardOwner",
      "orderId": "order123"
    }
  ]
}
```
#### Validate Card
```bash
grpcurl -plaintext -d '{"cardNumber": "1234-1234-1234-1234", "cardOwner": "CardOwner"}'  localhost:50080 card.CardService.validateCard
```
=>
```
{
  "value": true
}
```

