export type TInvoice = {
  id: string;
  invoice_number: number;
  supplier_id: string;
  issue_date: string;
  product_name: string;
  product_category: string;
  quantity: number;
  total_amount: number;
}