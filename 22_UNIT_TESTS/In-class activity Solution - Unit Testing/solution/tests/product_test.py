import unittest

from models.gender import Gender
from models.product import Product

VALID_NAME = 'TestName'
VALID_BRAND = 'TestBrand'
VALID_PRICE = 3.5
VALID_GENDER = Gender.UNISEX

EXPECTED_OUTPUT = (
    f''' #{VALID_NAME} {VALID_BRAND}
 #Price: ${VALID_PRICE:.2f}
 #Gender: {VALID_GENDER.value}
 ===''')


class Product_Should(unittest.TestCase):
    def test_constructor_raisesError_when_nameLengthOutOfBounds(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            _ = Product('_', VALID_BRAND, VALID_PRICE, VALID_GENDER)

    def test_constructor_raisesError_when_brandLengthOutOfBounds(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            _ = Product(VALID_NAME, '_', VALID_PRICE, VALID_GENDER)

    def test_constructor_raiseError_when_priceIsNegative(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            _ = Product(VALID_NAME, VALID_BRAND, -1.5, VALID_GENDER)

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        # Arrange & Act
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Assert
        self.assertEqual(VALID_NAME, product.name)
        self.assertEqual(VALID_BRAND, product.brand)
        self.assertEqual(VALID_PRICE, product.price)
        self.assertEqual(VALID_GENDER, product.gender)

    def test_nameSetter_changesName(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)
        expected = 'ValidName'

        # Act
        product.name = expected

        # Assert
        self.assertEqual(expected, product.name)

    def test_nameSetter_raisesError_nameTooShort(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        with self.assertRaises(ValueError):
            product.name = 'aa'

    def test_nameSetter_raisesError_nameTooLong(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        with self.assertRaises(ValueError):
            product.name = 'a' * 11

    def test_brandSetter_changesBrand(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)
        expected = 'ValidName'

        # Act
        product.brand = expected

        # Assert
        self.assertEqual(expected, product.brand)

    def test_brandSetter_raisesError_brandTooShort(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        with self.assertRaises(ValueError):
            product.brand = 'a'

    def test_brandSetter_raisesError_brandTooLong(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        with self.assertRaises(ValueError):
            product.brand = 'a' * 11

    def test_priceSetter_changesPrice(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)
        expected = 20.0

        # Act
        product.price = expected

        # Assert
        self.assertEqual(expected, product.price)

    def test_priceSetter_raisesError_priceTooLow(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        with self.assertRaises(ValueError):
            product.price = -5

    def test_toString_returnsCorrectlyFormattedString(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        self.assertEqual(EXPECTED_OUTPUT, product.to_string())
