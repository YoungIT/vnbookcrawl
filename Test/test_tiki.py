def test_readBook_1(tiki_fixture):

    result = tiki_fixture.readBooks( (52789367, 52789368) )

    assert result == {'title': 'Nhà Giả Kim (Tái Bản 2020)', 
                    'image_url': 'https://salt.tikicdn.com/cache/280x280/ts/product/45/3b/fc/aa81d0a534b45706ae1eee1e344e80d9.jpg', 
                    'genere': 'Văn học kinh điển – cổ điển', 
                    'author': 'Paulo Coelho,', 
                    'publisher': 'Nhã Nam', 'price': 51350, 
                    'description': 'Sơ lược về tác phẩmTất cả những trải nghiệm trong chuyến phiêu du theo đuổi vận mệnh của mình đã giúp Santiago thấu hiểu được ý nghĩa sâu xa nhất của hạnh phúc, hòa hợp với vũ trụ và con người.Tiểu ...', 
                    'translator': 'Bìa mềm', 
                    'num_pages': 'Nhà Xuất Bản Hà Nội'}

def test_readBook_2(tiki_fixture):

    pass



