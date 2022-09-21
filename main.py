def main():
    Datos={
"DueDate": "2022-02-24",
"Balance": 1990.19,
"DocNumber": "1053811422",
"Status": "Payable",
"Line": [
{
"Description": "Sample Expense",
"Amount": 500,
"DetailType": "ExpenseDetail",
"ExpenseDetail": {
"Customer": {
"value": "ABC123",
"name": "Sample Customer",
"Ref": {
"value": "DEF234",
"name": "Sample Construction",
"Address": {
"city": "Manizales",
"code_zip": "170002, 170001, 170003, 170004",
}
}
},
"LineStatus": "Billable"
}
}
],
"TotalAmt": 1990.19
}
    
    

if __name__=='__main__':
    main()