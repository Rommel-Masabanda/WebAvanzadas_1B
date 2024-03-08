import { CarritoDTO } from "./carritoDTO";
import { CartProductDTO } from "./cartProductDTO";

export interface cartDTO{
    carritos: CarritoDTO[],
    carrito_productos: CartProductDTO[]
}