/**
 * Time Conversion - Challenge 3 - Week 1
 * https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem
 * 
 * @param s - A time string in the form 12:40:22AM
 * @returns - A 'military' formatted time 00:40:22
 * 
 * @example
 * timeConversion("12:40:22AM") // "00:40:22"
 * timeConversion("07:05:45PM") // "19:05:45"
 */
export function timeConversion(s:string): string {
    // get into parts
    const [, hourStr, minStr, secStr, period] =
    s.match(/^(\d{2}):(\d{2}):(\d{2})(AM|PM)$/)!;

    // hour is the target of our meddling.
    let hour = parseInt(hourStr);

    // if period is PM add 12 to hour.
    if (period === "PM" && hour !== 12) hour += 12;

    // if period is AM and hour is twelve, then it moves to zero.
    if (period === "AM" && hour === 12) hour = 0;

    // format and return
    return `${hour.toString().padStart(2, "0")}:${minStr}:${secStr}`;
}