import type { Metadata } from "next";

import Header from "../components/Header";
import {
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
  Breadcrumbs,
  Tooltip,
  Stack,
  IconButton,
} from "@mui/material";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";

import VisibilityIcon from "@mui/icons-material/Visibility";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete"

import accountPayableData from "../_mock/account-payable.json";
import { TAccountPayable } from "../types/TAccountPayable";


export const metadata: Metadata = {
  title: "Lucro Rural",
  description: "Teste de admissão na Lucro Rural",
};

export default function Home() {

  return (
    <Box>
      <Header />

      <Box
        sx={{
          maxWidth: 1100,
          mx: "auto",
          mt: 3,
          mb: 2,
        }}
      >
        <Breadcrumbs aria-label="breadcrumb">
          <Typography color="text.primary" role="heading" fontSize={20} fontWeight={800}>
            Conta a Pagar
          </Typography>
        </Breadcrumbs>
      </Box>

      <TableContainer
        component={Paper}
        sx={{
          maxWidth: 1100,
          mx: "auto",
          mt: 4,
          backgroundColor: "#f9fafb",
          borderRadius: 2,
          border: "1px solid #e5e7eb",
          boxShadow: "0 1px 2px rgba(0,0,0,0.04)",
        }}
        elevation={0}
      >
        <Table>
          <TableHead>
            <TableRow>
              <TableCell align="left">
                <Typography fontWeight={600}>Ações</Typography>
              </TableCell>
              <TableCell align="left">
                <Typography fontWeight={600}>ID</Typography>
              </TableCell>
              <TableCell align="left">
                <Typography fontWeight={600}>Fornecedor</Typography>
              </TableCell>
              <TableCell align="left">
                <Typography fontWeight={600}>Data de Vencimento</Typography>
              </TableCell>
              <TableCell align="left">
                <Typography fontWeight={600}>Pago</Typography>
              </TableCell>
              <TableCell align="left">
                <Typography fontWeight={600}>Nota Fiscal</Typography>
              </TableCell>
              <TableCell align="left">
                <Typography fontWeight={600}>Total</Typography>
              </TableCell>
            </TableRow>
          </TableHead>

          <TableBody>
            {accountPayableData.map((account: TAccountPayable) => (
              <TableRow key={account.id} sx={{ "& td": { py: 2 } }}>
                <TableCell align="center">
                  <Stack direction="row" spacing={0.5} justifyContent="center">
                    {/* View */}
                    <Tooltip title="Visualizar">
                      <IconButton
                        size="small"
                      >
                        <VisibilityIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>

                    {/* Edit */}
                    <Tooltip title="Editar">
                      <IconButton
                        size="small"
                      >
                        <EditIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>

                    {/* Delete */}
                    <Tooltip title="Excluir">
                      <IconButton
                        size="small"
                        color="error"
                      >
                        <DeleteIcon fontSize="small" />
                      </IconButton>
                    </Tooltip>
                  </Stack>
                </TableCell>
                <TableCell>{account.id}</TableCell>
                <TableCell>{account.supplier.name}</TableCell>
                <TableCell>{account.deadline}</TableCell>
                <TableCell>
                  <Tooltip title={account.is_paid ? "Pago" : "Em aberto"}>
                    {account.is_paid ? (
                      <CheckCircleIcon
                        sx={{ color: "success.main" }}
                        fontSize="small"
                      />
                    ) : (
                      <CancelIcon
                        sx={{ color: "error.main" }}
                        fontSize="small"
                      />
                    )}
                  </Tooltip>
                </TableCell>
                <TableCell>
                  {account.invoices.map(inv => inv.invoice_number).join(", ")}
                </TableCell>
                <TableCell>R$ {account.total_amount.toFixed(2)}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}