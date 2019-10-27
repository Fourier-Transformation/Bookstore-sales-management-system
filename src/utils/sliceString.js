export function sliceString(str, length=50) {
    return str.length > length ? `${ str.slice(0, length) }...` : str;
}