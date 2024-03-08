import { ProductoGet } from "../producto/productoGet"
import { CarritoDTO } from "./carritoDTO"

export interface CarritoProductoDTO {
    carrito: CarritoDTO
    producto: ProductoGet
    cantidad: number
}