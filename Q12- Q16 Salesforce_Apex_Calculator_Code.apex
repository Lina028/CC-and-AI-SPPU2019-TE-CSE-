
// 12. Addition of Two Numbers in Salesforce (Apex)

public class Calculator {
    // Method to perform addition
    public static Integer addNumbers(Integer num1, Integer num2) {
        return num1 + num2;
    }
}

// Execute the Code in Salesforce Developer Console:
// System.debug(Calculator.addNumbers(10, 5)); // Output: 15

// ---

// 13. Subtraction of Two Numbers in Salesforce (Apex)

public class Calculator {
    // Method to perform subtraction
    public static Integer subtractNumbers(Integer num1, Integer num2) {
        return num1 - num2;
    }
}

// Execute the Code in Salesforce Developer Console:
// System.debug(Calculator.subtractNumbers(10, 5)); // Output: 5

// ---

// 14. Multiplication of Two Numbers in Salesforce (Apex)

public class Calculator {
    // Method to perform multiplication
    public static Integer multiplyNumbers(Integer num1, Integer num2) {
        return num1 * num2;
    }
}

// Execute the Code in Salesforce Developer Console:
// System.debug(Calculator.multiplyNumbers(10, 5)); // Output: 50

// ---

// 15. Division of Two Numbers in Salesforce (Apex)

public class Calculator {
    // Method to perform division
    public static Double divideNumbers(Integer num1, Integer num2) {
        if (num2 != 0) {
            return (Double)num1 / num2;
        } else {
            System.debug('Division by zero is not allowed.');
            return null; // Handle division by zero
        }
    }
}

// Execute the Code in Salesforce Developer Console:
// System.debug(Calculator.divideNumbers(10, 2)); // Output: 5.0
// System.debug(Calculator.divideNumbers(10, 0)); // Output: Division by zero is not allowed.

// ---

// 16. Perform All Operations (Addition, Subtraction, Multiplication, Division) on Two Numbers

public class Calculator {
    
    // Method to perform addition
    public static Integer addNumbers(Integer num1, Integer num2) {
        return num1 + num2;
    }
    
    // Method to perform subtraction
    public static Integer subtractNumbers(Integer num1, Integer num2) {
        return num1 - num2;
    }

    // Method to perform multiplication
    public static Integer multiplyNumbers(Integer num1, Integer num2) {
        return num1 * num2;
    }

    // Method to perform division
    public static Double divideNumbers(Integer num1, Integer num2) {
        if (num2 != 0) {
            return (Double)num1 / num2;
        } else {
            System.debug('Division by zero is not allowed.');
            return null;
        }
    }
    
    // Method to perform all operations and return a map of results
    public static Map<String, Object> performAllOperations(Integer num1, Integer num2) {
        Map<String, Object> result = new Map<String, Object>();
        result.put('Addition', addNumbers(num1, num2));
        result.put('Subtraction', subtractNumbers(num1, num2));
        result.put('Multiplication', multiplyNumbers(num1, num2));
        result.put('Division', divideNumbers(num1, num2));
        return result;
    }
}

// Execute the Code in Salesforce Developer Console:
// Map<String, Object> results = Calculator.performAllOperations(10, 5);
// System.debug('Addition: ' + results.get('Addition')); // Output: 15
// System.debug('Subtraction: ' + results.get('Subtraction')); // Output: 5
// System.debug('Multiplication: ' + results.get('Multiplication')); // Output: 50
// System.debug('Division: ' + results.get('Division')); // Output: 2.0
