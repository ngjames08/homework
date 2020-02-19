
Sub Easy_Stock()

    Dim Ticker As Double
    Dim Total_Volume As Double
 

    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Total Stock Volume"

    Ticker = 2
    Cells(Ticker, 9).Value = Cells(Ticker,1).Value

    LastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For Row = 2 To LastRow

    If Cells(Row, 1).Value = Cells(Ticker, 9) Then
    
    Total_Volume = Total_Volume + Cells(Row, 7).Value
     
    Else
     
    Cells(Ticker, 10).Value = Total_Volume
    Total_Volume = Cells(Row, 7).Value
    Ticker = Ticker + 1
    Cells(Ticker, 9).Value = Cells(Row, 1).Value
    End If
     
    Next Row
     
    Cells(Ticker, 10).Value = Total_Volume

End Sub