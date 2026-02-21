"use client";

import { useStock } from "../../hooks/useStockData";

type StockRow = {
  Date: string;
  Close: number;
  signal?: string;
};

export default function Dashboard() {
  const stock = useStock("AAPL") as StockRow[] | null;

  if (!stock) return <div>Loading...</div>;

  return (
    <div style={{ padding: "20px", fontFamily: "sans-serif" }}>
      <h1>AAPL Dashboard</h1>

      <table border={1} cellPadding={8}>
        <thead>
          <tr>
            <th>Date</th>
            <th>Close</th>
            <th>Signal</th>
          </tr>
        </thead>
        <tbody>
          {stock.slice(-10).map((row, i) => (
            <tr key={i}>
              <td>{new Date(row.Date).toLocaleDateString()}</td>
              <td>{row.Close.toFixed(2)}</td>
              <td>{row.signal ?? "-"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
