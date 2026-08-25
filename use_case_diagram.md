# Customizable Subscription Box Scheduler — UML Use-Case Diagram

## Problem Statement #35 | Retail, E-Commerce & Finance

**Actors:** Subscriber, Fulfillment Lead

---

## Use-Case Diagram

```mermaid
@startuml

left to right direction
skinparam packageStyle rectangle

actor "Subscriber" as Sub
actor "Fulfillment Lead" as FL

rectangle "Customizable Subscription Box Scheduler" {

  usecase "Manage Preference Tags" as UC1
  usecase "Customize Monthly Box" as UC2
  usecase "Pause / Skip Billing Cycle" as UC3
  usecase "View Subscription Status" as UC4
  usecase "Receive Renewal Notification" as UC5
  usecase "View Fulfillment Manifest" as UC6
  usecase "Export Fulfillment Manifest" as UC7
  usecase "Validate Customization Window" as UC8
  usecase "Apply Preference-Based Recommendations" as UC9

  Sub -- UC1
  Sub -- UC2
  Sub -- UC3
  Sub -- UC4
  Sub -- UC5

  FL -- UC6
  FL -- UC7

  UC2 ..> UC8 : <<include>>
  UC2 ..> UC9 : <<include>>
  UC3 ..> UC8 : <<include>>

  UC6 <.. UC7 : <<extend>>
}

@enduml
```

---

## Use-Case Descriptions (Summary)

| Use Case | Actor(s) | Description |
|----------|----------|-------------|
| Manage Preference Tags | Subscriber | Add, update, or remove preference tags (e.g., "vegan", "dark roast") to personalize recommendations. |
| Customize Monthly Box | Subscriber | Swap, add, or remove items in the upcoming monthly box before the 48-hour cutoff. |
| Pause / Skip Billing Cycle | Subscriber | Skip the next billing cycle without cancelling; subscription auto-resumes the following cycle. |
| View Subscription Status | Subscriber | View current subscription plan, billing dates, delivery history, and skip status. |
| Receive Renewal Notification | Subscriber | Receive email and in-app reminder 72 hours before billing renewal with current box summary. |
| View Fulfillment Manifest | Fulfillment Lead | View monthly manifest listing all active subscriber orders, items, and shipping addresses. |
| Export Fulfillment Manifest | Fulfillment Lead | Export the manifest as CSV/PDF with shipping labels for warehouse/logistics partners. |
| Validate Customization Window | System (included) | Check that the current time is at least 48 hours before the billing renewal date before allowing changes. |
| Apply Preference-Based Recommendations | System (included) | Generate personalized product suggestions based on the subscriber's preference tags. |

---

## Relationships

| Relationship | Type | Explanation |
|--------------|------|-------------|
| Customize Monthly Box → Validate Customization Window | **«include»** | Every customization attempt must first verify the subscriber is within the allowed modification window (≥ 48 hours before renewal). This is a mandatory check. |
| Customize Monthly Box → Apply Preference-Based Recommendations | **«include»** | When a subscriber opens the customization page, the system always loads personalized recommendations based on their tags. This is integral to the customization flow. |
| Pause / Skip Billing Cycle → Validate Customization Window | **«include»** | Skipping a cycle also requires the 48-hour window validation, as the problem statement ties pausing to the same cutoff. |
| View Fulfillment Manifest ← Export Fulfillment Manifest | **«extend»** | Exporting is an optional extension of viewing the manifest. The Fulfillment Lead may view without exporting, but export always extends from the view context. |
