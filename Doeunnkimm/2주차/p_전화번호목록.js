function solution(phone_book) {
  phone_book.sort()

  const isPrefix = phone_book.some((book, idx) => {
    return phone_book[idx + 1]?.startsWith(book)
  })

  return !isPrefix
}

/**
 * 📝 NOTE
 *
 * 1.
 * JavaScript를 sort하게 되면 맨 앞 숫자부터 비교를 하기 때문에
 *
 * ["119", "97674223", "1195524421"]을 sort하게 되면
 * ["119", "1195524421", "97674223"]가 된다.
 *
 * 2.
 * some()은 하나라도 true라면 true를 반환하고
 * every()는 전부 true여야 true를 반환한다.
 */
