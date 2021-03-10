var Woocommerce = WC.WC()

        Woocommerce.get('orders', function (err, data, res) {
            if (err):
                print(err);

            print(JSON.parse(res));