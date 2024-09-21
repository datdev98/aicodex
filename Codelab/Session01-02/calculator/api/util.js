/**
 * Function to convert 2 dimention array to 1 string
 *
 * Example:
 * 2D array: [[1, 2], [3, 4]]
 * String: '1234'
 */
function convert2DArrayToString(arr) {
    // TODO: Implement this function
    // Return string not array
    return arr.map(row => row.join('')).join('');
}