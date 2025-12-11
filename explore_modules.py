import agent_framework

print("MICROSOFT AGENT FRAMEWORK - MODULE EXPLORATION")

# List all available modules
print("\nAvailable modules in agent_framework:")
import pkgutil
for module in pkgutil.iter_modules(agent_framework.__path__):
    print(f"  - {module.name}")

# Check key classes
print("\nKey Classes:")
print(f"  - ChatAgent: {hasattr(agent_framework, 'ChatAgent')}")
print(f"  - ChatMessage: {hasattr(agent_framework, 'ChatMessage')}")
print(f"  - AIFunction: {hasattr(agent_framework, 'AIFunction')}")

# Check for workflow support
print("\nWorkflow Support:")
try:
    from agent_framework import AgentWorkflow
    print("  ✅ AgentWorkflow available")
except ImportError:
    print("  AgentWorkflow not found")

# Check for observability
print("\n Observability:")
try:
    from agent_framework import observability
    print("  ✅ Observability module available")
except ImportError:
    print("  Observability not found")
