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
} from "@mui/material";

export const metadata: Metadata = {
  title: "Lucro Rural",
  description: "Teste de admissão na Lucro Rural",
};

export default function Home() {
  return (
    <Box>
      <Header />

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
              <TableCell />
              <TableCell align="right">
                <Typography fontWeight={600}>Receitas</Typography>
              </TableCell>
              <TableCell align="right">
                <Typography fontWeight={600}>Despesas</Typography>
              </TableCell>
              <TableCell align="right">
                <Typography fontWeight={600}>Resultado</Typography>
              </TableCell>
            </TableRow>
          </TableHead>

          <TableBody>
            <TableRow
              sx={{
                "& td": {
                  py: 2,
                },
              }}
            >
              <TableCell>
                <Typography fontWeight={500}>Realizado</Typography>
              </TableCell>

              <TableCell align="right" sx={{ color: "success.main" }}>
                R$ 6.880.603,92
              </TableCell>

              <TableCell align="right" sx={{ color: "error.main" }}>
                R$ 5.737.229,86
              </TableCell>

              <TableCell
                align="right"
                sx={{ color: "success.main", fontWeight: 600 }}
              >
                R$ 1.143.374,06
              </TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}