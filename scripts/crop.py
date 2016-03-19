from PIL import Image







n = 0
while n<8:
    print n
    test_image = "/home/myroslav/reserv/reserv/visareserv/screenshot/screed/%d.png" % n
    original = Image.open(test_image)
    box = (569, 89, 982, 596)
    cropped_example = original.crop(box)
    cropped_example.save("/home/myroslav/reserv/reserv/visareserv/screenshot/res/%d.png" % n, 'png')
    n += 1


