"use client";
import { useState } from 'react';
import { Calculator, Plus, Minus, X, Divide, Delete, Equal, Percent, Square } from 'lucide-react';

export default function CalculatorPage() {
  const [displayValue, setDisplayValue] = useState<string>('0');
  const [firstOperand, setFirstOperand] = useState<string | null>(null);
  const [operator, setOperator] = useState<string | null>(null);
  const [waitingForSecondOperand, setWaitingForSecondOperand] = useState<boolean>(false);

  const inputDigit = (digit: string) => {
    if (waitingForSecondOperand) {
      setDisplayValue(digit);
      setWaitingForSecondOperand(false);
    } else {
      setDisplayValue(displayValue === '0' ? digit : displayValue + digit);
    }
  };

  const inputDecimal = () => {
    if (waitingForSecondOperand) {
      setDisplayValue('0.');
      setWaitingForSecondOperand(false);
      return;
    }

    if (!displayValue.includes('.')) {
      setDisplayValue(displayValue + '.');
    }
  };

  const clearDisplay = () => {
    setDisplayValue('0');
    setFirstOperand(null);
    setOperator(null);
    setWaitingForSecondOperand(false);
  };

  const handleOperator = (nextOperator: string) => {
    const inputValue = parseFloat(displayValue);

    if (firstOperand === null) {
      setFirstOperand(inputValue.toString());
    } else if (operator) {
      const currentValue = firstOperand || '0';
      const result = performCalculation[operator](parseFloat(currentValue), inputValue);

      setDisplayValue(result.toString());
      setFirstOperand(result.toString());
    }

    setWaitingForSecondOperand(true);
    setOperator(nextOperator);
  };

  const performCalculation = {
    '+': (a: number, b: number) => a + b,
    '-': (a: number, b: number) => a - b,
    '*': (a: number, b: number) => a * b,
    '/': (a: number, b: number) => a / b,
  };

  const calculateResult = () => {
    if (firstOperand === null || operator === null) return;

    const inputValue = parseFloat(displayValue);
    const result = performCalculation[operator](parseFloat(firstOperand), inputValue);

    setDisplayValue(result.toString());
    setFirstOperand(null);
    setOperator(null);
    setWaitingForSecondOperand(false);
  };

  const handlePercentage = () => {
    const value = parseFloat(displayValue) / 100;
    setDisplayValue(value.toString());
  };

  const handleSquare = () => {
    const value = parseFloat(displayValue);
    setDisplayValue((value * value).toString());
  };

  return (
    <div className="w-full max-w-md mx-auto">
      <div className="bg-white rounded-xl shadow-lg overflow-hidden">
        <div className="p-6 bg-primary-600 text-white">
          <div className="flex items-center justify-center mb-4">
            <Calculator className="w-8 h-8 mr-2" />
            <h1 className="text-2xl font-bold">MiniCalc</h1>
          </div>
          <div className="text-right text-4xl font-medium mb-2 truncate">
            {displayValue}
          </div>
        </div>

        <div className="grid grid-cols-4 gap-1 p-4 bg-gray-100">
          <button
            className="p-4 bg-gray-200 rounded-lg hover:bg-gray-300 transition-colors"
            onClick={clearDisplay}
          >
            <Delete className="mx-auto" />
          </button>
          <button
            className="p-4 bg-gray-200 rounded-lg hover:bg-gray-300 transition-colors"
            onClick={handleSquare}
          >
            <Square className="mx-auto" />
          </button>
          <button
            className="p-4 bg-gray-200 rounded-lg hover:bg-gray-300 transition-colors"
            onClick={handlePercentage}
          >
            <Percent className="mx-auto" />
          </button>
          <button
            className="p-4 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors"
            onClick={() => handleOperator('/')}
          >
            <Divide className="mx-auto" />
          </button>

          {['7', '8', '9'].map((digit) => (
            <button
              key={digit}
              className="p-4 bg-white rounded-lg hover:bg-gray-200 transition-colors"
              onClick={() => inputDigit(digit)}
            >
              {digit}
            </button>
          ))}

          <button
            className="p-4 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors"
            onClick={() => handleOperator('*')}
          >
            <X className="mx-auto" />
          </button>

          {['4', '5', '6'].map((digit) => (
            <button
              key={digit}
              className="p-4 bg-white rounded-lg hover:bg-gray-200 transition-colors"
              onClick={() => inputDigit(digit)}
            >
              {digit}
            </button>
          ))}

          <button
            className="p-4 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors"
            onClick={() => handleOperator('-')}
          >
            <Minus className="mx-auto" />
          </button>

          {['1', '2', '3'].map((digit) => (
            <button
              key={digit}
              className="p-4 bg-white rounded-lg hover:bg-gray-200 transition-colors"
              onClick={() => inputDigit(digit)}
            >
              {digit}
            </button>
          ))}

          <button
            className="p-4 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors"
            onClick={() => handleOperator('+')}
          >
            <Plus className="mx-auto" />
          </button>

          <button
            className="col-span-2 p-4 bg-white rounded-lg hover:bg-gray-200 transition-colors"
            onClick={() => inputDigit('0')}
          >
            0
          </button>

          <button
            className="p-4 bg-white rounded-lg hover:bg-gray-200 transition-colors"
            onClick={inputDecimal}
          >
            .
          </button>

          <button
            className="p-4 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors"
            onClick={calculateResult}
          >
            <Equal className="mx-auto" />
          </button>
        </div>
      </div>
    </div>
  );
}