def thousand_comma(value):
    # 숫자를 문자열로 변환
    value_str = str(value)

    # 소수점 위치 확인
    if '.' in value_str:
        integer_part, decimal_part = value_str.split('.')
    else:
        integer_part, decimal_part = value_str, None

    # 정수 부분에 천단위 콤마 추가
    result = ""
    for i, digit in enumerate(reversed(integer_part)):
        if i > 0 and i % 3 == 0:
            result += ','
        result += digit

    # 결과를 뒤집어서 반환
    result_with_comma = result[::-1]

    # 소수점 처리
    if decimal_part is not None:
        result_with_comma += '.' + decimal_part

    return result_with_comma
