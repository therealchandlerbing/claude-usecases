'use client';

import { useState, useEffect, useCallback } from 'react';

/**
 * Hook for persisting state in localStorage with SSR support.
 *
 * @param key - localStorage key
 * @param initialValue - Default value if key doesn't exist
 * @returns [value, setValue, removeValue]
 *
 * @example
 * const [theme, setTheme] = useLocalStorage('theme', 'light');
 */
export function useLocalStorage<T>(
  key: string,
  initialValue: T
): [T, (value: T | ((val: T) => T)) => void, () => void] {
  // State to store our value
  const [storedValue, setStoredValue] = useState<T>(initialValue);
  const [isInitialized, setIsInitialized] = useState(false);

  // Initialize from localStorage after mount (SSR safe)
  useEffect(() => {
    try {
      const item = window.localStorage.getItem(key);
      if (item) {
        setStoredValue(JSON.parse(item));
      }
    } catch (error) {
      console.warn(`Error reading localStorage key "${key}":`, error);
    }
    setIsInitialized(true);
  }, [key]);

  // Save to localStorage when value changes
  useEffect(() => {
    if (!isInitialized) return;

    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue));
    } catch (error) {
      console.warn(`Error setting localStorage key "${key}":`, error);
    }
  }, [key, storedValue, isInitialized]);

  // Setter function
  const setValue = useCallback(
    (value: T | ((val: T) => T)) => {
      setStoredValue((prev) =>
        value instanceof Function ? value(prev) : value
      );
    },
    []
  );

  // Remove from localStorage
  const removeValue = useCallback(() => {
    try {
      window.localStorage.removeItem(key);
      setStoredValue(initialValue);
    } catch (error) {
      console.warn(`Error removing localStorage key "${key}":`, error);
    }
  }, [key, initialValue]);

  return [storedValue, setValue, removeValue];
}

export default useLocalStorage;
