# Architecture Decision Record

| # | Decision | Alternatives considered | Reason chosen |
|---|----------|-------------------------|---------------|
| 1 | Keep the app as a desktop Tkinter project | Web app, CLI script | The original repo was already a simple desktop toy, so preserving that keeps the spirit intact while improving structure. |
| 2 | Split UI from story logic | Single-file script | This makes the app testable and easier to extend without breaking the interface. |
| 3 | Add multiple templates instead of changing the original prompt only | Keep exactly one template | The original remains as the default, while extra templates improve replay value and UX. |
