# Architecture Guidelines — TEMPLATE

> **⚠️ TEMPLATE FILE — Replace with your actual architecture decisions**

## Tech Stack
| Layer | Technology | Reason |
|-------|-----------|--------|
| Frontend | [e.g., Next.js 16 App Router] | [why] |
| Styling | [e.g., Tailwind CSS + Shadcn UI] | [why] |
| Backend/ORM | [e.g., Prisma + PostgreSQL] | [why] |
| Auth | [e.g., Supabase Auth] | [why] |
| Hosting | [e.g., Vercel] | [why] |

## Folder Structure
```
/
├── app/          # Next.js App Router pages
├── components/   # Reusable UI components
├── lib/          # Utilities, db client, helpers
└── prisma/       # Database schema & migrations
```

## Key Architecture Decisions
1. [Decision 1 and why you made it]
2. [Decision 2 and why you made it]

## Constraints
- [e.g., Must work without Docker]
- [e.g., No server-side rendering for dashboard routes]