'use client'

import { createContext, useState, useEffect, useContext } from 'react'

type Theme = 'dark' | 'light' | 'system'

type ThemeContextType = {
    theme: Theme
    toggleTheme: () => void
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined)

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {

    const getSystemTheme = () => {
        if (typeof window === "undefined") return "light"

        return window.matchMedia("(prefers-color-scheme: dark)").matches
            ? "dark"
            : "light"
    }

    const [theme, setTheme] = useState<Theme>(() => {
        if (typeof window === "undefined") return "system"

        const saved = localStorage.getItem("theme") as Theme | null
        return saved ?? "system"
    })

    useEffect(() => {
        const root = document.documentElement
        console.log(theme);

        const appliedTheme = theme === "system"
            ? getSystemTheme()
            : theme

        if (appliedTheme === "dark") {
            root.classList.add("dark")
        } else {
            root.classList.remove("dark")
        }

        localStorage.setItem("theme", theme)

    }, [theme])

    const toggleTheme = () => {
        setTheme(prev => prev === "light" ? "dark" : "light")
    }

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    )
}

export const useTheme = () => {
    const context = useContext(ThemeContext)

    if (!context) {
        throw new Error("useTheme must be used within ThemeProvider")
    }

    return context
}