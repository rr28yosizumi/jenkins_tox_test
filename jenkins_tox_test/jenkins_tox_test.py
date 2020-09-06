"""Main module."""

def realnum_format(x,n=8):
    """
    xの文字列で指定した数値を少数点n桁目まで0埋めした文字列を返す
    ただし、xが小数点n+1桁以上あれば、n桁目以降は切り捨てる
    """
    return ('{:.'+str(n)+'f}').format(
        float(
            # 少数点がなければ、そのまま。小数点があれば、少数n桁までをスライスする
            x[:min(x.find('.')+1+n,len(x))] if '.' in x else x
        )
    )
