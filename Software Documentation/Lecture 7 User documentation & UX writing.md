midterm - 9th week
## Diataxis Framework
industry leading framework for structuring technical documentation. it defines four distinct documentation types each serving a different user need and mental mode.
![[Pasted image 20261013112130.png]]
## 4 documentation types explained 
### Tutorial 
Learning-oriented. Guides a newcomer through a hands on experience. the user learns by doing. success = completing the tutorial, not understanding everything.
Example: *"Build your first API call in 10 minutes"*
### How to guide
Task-oriented. directs a competent user to accomplish a specific goal. assumes prior knowledge. Focuses on steps not explanation.
Example: *"How to reset a user password"*
### Reference
Information-oriented. Dry, accurate, complete. Users consult it while working. No narrative- just facts, parameters, and return values
Example: *"API endpoint table with all parameters"
### Explanation
Understanding-oriented. Discusses background, context and design decisions. Helps users build a mental model. Not task-driven.
Example: *"Why we use JWT over session cookies"*

## Why Diataxis matters in practice
Core insight
Most documentation failures happen because writers mix types. A tutorial that explains theory loses the learner. A how to that teaches concepts wastes the expert's time. Diataxis forces you to ask. What mode is my user in right now ? 

Each type lives in a separate section of your docs site. User self-select based on their current need - not your assumptions about them.
1. Stripe docs - industry gold standard - strict Diaxatric separation across all products.
2. Django docs - Tutorial -> how-to -> reference -> explanation clearly labeled.
3. Read the docs -> Platform built around Diataxis- compatible structure by default

## UX writing: words are part of the interface
Every word in your product - buttons, errors, prompts - shapes the user experience.
1. microcopy - use specific, purposeful labels - "Create account" beats "submit" every time 
2. Error messages - always tell users what went wrong, why  and what to do next.
3. onboarding flows - Guide users to their first success quickly using progressive disclosure
! "Writing software documentation: A task oriented approach" - Thomas T. Barker

Алдааны мэдээллийг хэрэглэгчид ээлтэй байдлаар харуулах хэрэгтэй.
onboarding - хэрэглэгч ямар нэгэн үйлдлийг анх удаа амжилттай хийх
хэрэглэгчид бүх функцийг нэг дор харуулах хэрэггүй. (төлвийн менежмент хийх шаардлагатай.) Нэг удаа амжилтгүй үйлдэл хийгдсэний дараа дараагийн үйлдэл амжилттай болгох.

Good UX documentation decreases the pause of usage for users by guiding user properly.
## Hosting platforms : Publishing your docs
1. GitBook - git connected, beautiful UI, free for public projects. Best for user facing docs with minimal setup.
2. Read the Docs - open source standard. Sphinx/MkDocs integration. Auto-builds on every push. Versioning built in.
3. MkDocs/ Docusaurus - Static site generator. full control over structure and theme. Deploy to GitHub Pages or any CDN(Content Delivery Network)