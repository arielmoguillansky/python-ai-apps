# Coffee Machine Simulator

A command-line coffee machine application demonstrating core OOP principles in Python.

## Architecture

### Class Structure

**MenuItem**

- Encapsulates drink specifications (name, ingredients, cost)
- Immutable data model for menu items

**Menu**

- Manages collection of MenuItem objects
- Uses dictionary for O(1) drink lookup by name
- Returns MenuItem instances (not dictionaries)

**CoffeeMachine**

- Central controller handling resources, money, and state
- Maintains resource inventory (water, milk, coffee in ml/g)
- Tracks monetary transactions
- Validates resource availability before drink preparation

### Key Logic Flow

1. **Input Loop**: Continuously prompts user for drink selection
2. **Resource Check**: Validates sufficient ingredients via `is_resource_sufficient()`
3. **Payment Processing**: Calculates coin total (quarters/dimes/nickles/pennies), validates amount, computes change
4. **Drink Production**: Deducts ingredients from inventory, updates money counter

### Technical Decisions

- **Object Storage**: Menu stores MenuItem objects directly instead of unpacking to dictionaries (better encapsulation)
- **State Management**: Single CoffeeMachine instance maintains all state (resources, money, on/off status)
- **Error Handling**: Try-except block catches TypeError from invalid menu selections
- **Resource Tracking**: Dictionary-based inventory allows dynamic ingredient checking

### Data Flow

```
User Input → Menu Lookup → Resource Check → Payment → Production → Update State
```

### Limitations

- No persistence (state resets on restart)
- Basic error handling (doesn't catch ValueError for coin inputs)
- US currency only
- No refund mechanism for failed production

## Usage

```bash
python main.py
```

Commands: `espresso`, `latte`, `cappuccino`, `report`, `turn off`
