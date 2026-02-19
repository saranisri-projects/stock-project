import { useEffect, useState } from "react";
import { getStock, StockPoint } from "../api/stocks";

export function useStock(symbol: string) {
  const [data, setData] = useState<StockPoint[] | null>(null);

  useEffect(() => {
    getStock(symbol).then(setData);
  }, [symbol]);

  return data;
}
