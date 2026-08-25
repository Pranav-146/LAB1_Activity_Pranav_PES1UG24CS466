# Use-Case Flow Specification

## Use Case: Customize Monthly Box

| Field | Detail |
|-------|--------|
| **Use Case ID** | UC-002 |
| **Use Case Name** | Customize Monthly Box |
| **Primary Actor** | Subscriber |
| **Secondary Actor(s)** | System (Recommendation Engine, Fulfillment Service) |
| **Related Requirements** | FR-001, FR-002, FR-005 |
| **Description** | Allows a subscriber to swap, add, or remove items in their upcoming monthly subscription box based on personal preferences, provided the customization window is still open (≥ 48 hours before billing renewal). |

---

## Preconditions

1. The subscriber is registered and has an active (non-cancelled) subscription.
2. The subscriber is authenticated and logged into the portal.
3. The next billing cycle is scheduled, and the current date/time is **at least 48 hours before** the monthly billing renewal date.
4. A default box has been generated for the upcoming cycle based on the subscriber's preference tags.

---

## Postconditions

1. The subscriber's monthly box contents are updated to reflect the new selections.
2. The fulfillment manifest is refreshed to include the updated item list for this subscriber.
3. A confirmation notification (email + in-app) is sent to the subscriber summarizing the changes.
4. The inventory count for swapped-out items is restored and swapped-in items are reserved.

---

## Main Success Scenario

| Step | Actor | Action |
|------|-------|--------|
| 1 | Subscriber | Navigates to the "My Upcoming Box" page from the dashboard. |
| 2 | System | **«include» Validate Customization Window:** Checks that the current time is ≥ 48 hours before the billing renewal date. Validation passes. |
| 3 | System | **«include» Apply Preference-Based Recommendations:** Loads the current box contents alongside personalized product recommendations based on the subscriber's preference tags. |
| 4 | System | Displays the current box items, available alternative products (with preference-match scores), and the customization deadline. |
| 5 | Subscriber | Reviews the current box and selects one or more items to swap. For each swap, the subscriber picks a replacement from the recommended alternatives or browses the full catalog. |
| 6 | System | For each swap request, validates that the replacement item is in stock and compatible with the subscriber's subscription tier. |
| 7 | System | Updates the box preview in real time showing the new item(s), adjusted box summary, and any price difference (if applicable). |
| 8 | Subscriber | Reviews the updated box preview and confirms the changes by clicking "Save My Box." |
| 9 | System | Persists the updated box selections to the database. Releases inventory hold on removed items and reserves inventory for the newly selected items. |
| 10 | System | Refreshes the fulfillment manifest for the current billing cycle to reflect the subscriber's updated box contents. |
| 11 | System | Sends a confirmation notification (email + in-app) to the subscriber with the finalized box summary and expected delivery date. |
| 12 | System | Displays a success message: "Your box has been updated successfully!" |

---

## Alternate Flow: Customization Window Closed

| Step | Actor | Action |
|------|-------|--------|
| 2a | System | At Step 2, the system determines that the current time is **less than 48 hours** before the billing renewal date. The customization window has closed. |
| 2b | System | Displays a message: "The customization window for this cycle has closed. Your current box will be shipped as-is. You can still customize your next month's box after the current cycle renews." |
| 2c | System | Shows the current (locked) box contents in read-only mode, along with the date when customization for the next cycle will open. |
| 2d | Subscriber | Acknowledges the message. May choose to navigate to subscription settings to skip the current cycle (if skip window is also still open), or simply exit. |

---

## Exceptions

| ID | Condition | System Response |
|----|-----------|-----------------|
| E1 | Selected replacement item is out of stock. | System displays "This item is currently unavailable" and suggests the next-best alternative from the recommendation engine. |
| E2 | Database or network error during save. | System displays "We couldn't save your changes. Please try again." Changes are rolled back; inventory holds are not modified. |
| E3 | Session expires during customization. | System redirects to the login page. Unsaved changes are stored temporarily and restored upon re-authentication. |

---

## Business Rules

- **BR-01:** A subscriber may customize their box an unlimited number of times within the customization window. Only the final saved state is sent to fulfillment.
- **BR-02:** The customization window opens immediately after the previous cycle's billing renewal and closes 48 hours before the next renewal.
- **BR-03:** Price differences from item swaps (e.g., premium items) are reflected as add-on charges or credits on the next billing statement.
