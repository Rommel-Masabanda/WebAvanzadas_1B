export function getTokenLS(): string {
    return localStorage.getItem('token')??"";
}
