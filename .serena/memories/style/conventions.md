# Code Conventions — TEMPLATE

> **⚠️ TEMPLATE — Replace with your actual coding conventions**

## Naming Conventions
- **Components:** PascalCase (`UserCard.tsx`)
- **Hooks:** camelCase with `use` prefix (`useAuth.ts`)
- **Utils:** camelCase (`formatDate.ts`)
- **API routes:** kebab-case (`/api/user-profile`)

## Import Order
1. React/Next.js imports
2. Third-party libraries
3. Internal components
4. Utilities & types
5. Styles

## TypeScript Rules
- No `any` types
- Define interfaces for all props
- Use `type` for unions, `interface` for objects