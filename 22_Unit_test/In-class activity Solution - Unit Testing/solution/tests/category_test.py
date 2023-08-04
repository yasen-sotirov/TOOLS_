import unittest
from unittest.mock import Mock


from models.category import Category
from models.product import Product

VALID_NAME = 'Shampoo'


def create_product(fake_name = 'fake name'):
    product = Mock()
    product.name = fake_name
    product.to_string = lambda: fake_name

    return product


class Category_Should(unittest.TestCase):
    def test_constructor_raisesError_when_nameLengthOutOfBounds(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            _ = Category('x')

    def test_constructor_createsCategory_when_nameIsValid(self):
        # Arrange
        category = Category(VALID_NAME)

        # Act & Assert
        self.assertEqual(VALID_NAME, category.name)

    def test_nameSetter_changesName(self):
        # Arrange
        category = Category(VALID_NAME)
        expected = 'ValidName'

        # Act
        category.name = expected

        # Assert
        self.assertEqual(expected, category.name)

    def test_nameSetter_raisesError_nameTooShort(self):
        # Arrange
        category = Category(VALID_NAME)

        # Act & Assert
        with self.assertRaises(ValueError):
            category.name = 'aa'

    def test_nameSetter_raisesError_nameTooLong(self):
        # Arrange
        category = Category(VALID_NAME)

        # Act & Assert
        with self.assertRaises(ValueError):
            category.name = 'a' * 11

    def test_constructor_initializesCorrectProductsType_when_categoryCreated(self):
        # Arrange
        category = Category(VALID_NAME)

        # Act & Assert
        self.assertIsInstance(category.products, tuple)

    def test_addProduct_addsProductToList(self):
        # Arrange
        category = Category(VALID_NAME)
        # Act
        category.add_product(create_product())

        # Assert
        self.assertEqual(1, len(category.products))

    def test_addProduct_raisesError_whenSameProductAddedMoreThanOnce(self):
        # Arrange
        category = Category(VALID_NAME)
        category.add_product(create_product())

        with self.assertRaises(ValueError):
            # Act & Assert
            category.add_product(create_product())

    def test_removeProduct_removesProductFromList(self):
        # Arrange
        category = Category(VALID_NAME)
        category.add_product(create_product())

        # Act
        category.remove_product(create_product())

        # Assert
        self.assertEqual(0, len(category.products))

    def test_removeProduct_raiseError_whenProductDoesNotExist(self):
        # Arrange
        category = Category(VALID_NAME)

        # Act & Assert
        with self.assertRaises(ValueError):
            category.remove_product(create_product())

    def test_tostring_correctOutput_noProducts(self):
        # Arrange
        NEW_LINE = '\n'
        category = Category(VALID_NAME)
        expected = f'#Category: {VALID_NAME}{NEW_LINE} #No products in this category'

        # Act
        actual = category.to_string()

        # Assert
        self.assertEqual(expected, actual)

    def test_tostring_correctOutput_whenHasProducts(self):
        # Arrange
        NEW_LINE = '\n'
        PROD_OUTPUT_1 = 'prod1'
        PROD_OUTPUT_2 = 'prod2'
        category = Category(VALID_NAME)
        category.add_product(create_product(PROD_OUTPUT_1))
        category.add_product(create_product(PROD_OUTPUT_2))

        expected = f'#Category: {VALID_NAME}{NEW_LINE}{PROD_OUTPUT_1}{NEW_LINE}{PROD_OUTPUT_2}'

        # Act
        actual = category.to_string()

        # Assert
        self.assertEqual(expected, actual)
