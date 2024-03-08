import { ProductoCartDTO } from "../producto/productoCartDTO";
export interface CarritoDTO {
    id: number;
    total: number;
    cantidad_productos: number;
    usuario: number;
    productos: ProductoCartDTO[];
}