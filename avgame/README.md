# Strategy Pattern

This pattern abstracts specific features of a class or interface into small pieces that can be applied at run-time.

What this means is that you create a class (interface) as an abstract base class (ABC). With this class you define the blueprint all implementation of this class must follow. So long as future classes follow the ABC, they will function in the implemented code. The ABC defines a behavior that you want your super class to display.

In the case of this example, the ABC is `WeaponBehavior` and outlines how to define different types of weapons.  The weapons can perform any type of behavior they want, so long as they follow the ABC blueprint. For this case, they must have a `use_weapon()` method.

`WeaponBehavior` is now an interface. It is not inherited by `Character`, rather it is imported and used in composition. This is the key piece of defining behavior **at runtime** versus designing to the implementation and being locked into behavior.

For this example I choose to have `Character` use a setter method `set_weapon()` to change which of the four behaviors to request from the interface. I used a literal parameter though this could easily be on each of the `Character` objects children classes to import and pass in (**perhaps this would be better!**)

The `Character` superclass is defined with the setter method for choosing a behavior, and calls that behavior referencing the ABC. This is the contract. The superclass doesn't care about the interface so long as the interface upholds the contracted blueprint.

**The interface is completely encapsulated!**

Finally, the bulk of the code goes into `Character` which the children classes; Knight, King, Queen, and Troll; inheriting. They, then, set their weapon of choice and have full use of the pattern.

