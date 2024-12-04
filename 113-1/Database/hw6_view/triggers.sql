
Use FinanceDB
GO

CREATE TRIGGER trg_UpdateInvoiceStatus
ON Payment AFTER INSERT AS
BEGIN
    SET NOCOUNT ON;
    UPDATE Invoice
    SET status = 
        CASE 
            WHEN ( SELECT ISNULL(SUM(p.amount), 0) FROM Payment p WHERE p.invoice_id = Invoice.id
            ) >= Invoice.amount THEN 'Paid'
            ELSE status
        END
    WHERE id IN (
        SELECT DISTINCT invoice_id
        FROM inserted
    );

    UPDATE Invoice
    SET status = 'Overdue'
    WHERE due_date < GETDATE() AND status NOT IN ('Paid', 'Overdue');
END;
GO


