from dct import  DCT 


def test_plain_text():
    print('test_plain_text()')
    in_img = "test_imgs/mountain.png"
    msg = b"This is my secret"

    out_img = "mountain_DCT.png"


    en = DCT(in_img)
    en.DCTEn(msg, out_img)

    dec = DCT(out_img)
    secret  = dec.DCTDe()

    if secret != msg:
        raise AssertionError("Secret != msg")

    print('Passed!\n')


# test embeg img


def test_embed_img():
    print("test_embed_img()")
    in_img = "test_imgs/river.png"
    with open("test_imgs/face.jpg", "rb") as f:
        raw = f.read()

    out_img = "river_DCT.png"

    en = DCT(in_img)
    en.DCTEn(raw, out_img)

    dec = DCT(out_img)
    secret  = dec.DCTDe()


    if secret != raw:
        raise AssertionError("Secret face.jpg != original face.jpg")

    print('Passed!\n')

test_plain_text()

test_embed_img()









