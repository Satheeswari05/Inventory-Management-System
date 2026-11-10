
class InventoryError(Exception):
    """Base exception for inventory-related errors."""
    pass


class InvalidProductError(InventoryError):
    """Raised when product details are invalid."""
    pass


class ProductNotFoundError(InventoryError):
    """Raised when a product does not exist."""
    pass


class InsufficientStockError(InventoryError):
    """Raised when requested quantity exceeds available stock."""
    pass


class DuplicateProductError(InventoryError):
    """Raised when a product ID already exists."""
    pass
