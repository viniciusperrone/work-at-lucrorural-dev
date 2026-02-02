import { TInvoice } from "./TInvoice";
import { TSupplier } from "./TSupplier";

export type TAccountPayable = {
  id: string;
  supplier: TSupplier;
  deadline: string;
  is_paid: boolean;
  invoices: TInvoice[];
  total_amount: number;
}