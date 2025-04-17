export function timeConversion(s:string): string {
    console.log(s)
    // get into parts
    const [, hourStr, minStr, secStr, period] =
    s.match(/^(\d{2}):(\d{2}):(\d{2})(AM|PM)$/)!;

    // if last is PM add 12 to hour
    let hour = parseInt(hourStr);
    if (period === "PM" && hour !== 12) hour += 12;

    // fomat and return
    return `${hour}:${minStr}:${secStr}`
}