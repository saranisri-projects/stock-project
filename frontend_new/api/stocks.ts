export type StockPoint = {
  Date: string;
  Close: number;
  ma10: number | null;
  signal: "BUY" | "SELL" | "HOLD";
};

export async function getStock(symbol: string): Promise<StockPoint[]> {
  const res = await fetch(`http://127.0.0.1:8000/stocks/${symbol}`);
  return res.json();
}
