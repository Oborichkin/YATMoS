### Fixes:

- [ ] Cascase delete handling
- [ ] Unqiue constraints checking

### Add:

- [ ] Test Runs
- [ ] Tags
- [ ] Users
- [ ] Comments
- [ ] Milestones
- [ ] DB configuration
- [ ] Dockerfile
- [ ] GitHub Actions
- [x] Test Step reordering

### Look into:
  - [ ] Nested routers. ex: /project/{id}/suite/{id}/test/{id} == /suite/{id}/test/{id} == /test/{id}
  - [x] Order of children in one-to-many relationships
  - [ ] Referencing old versions of models (e.g. old test run references test case that has been changed later)

### New:
- [ ] Alembic
- [ ] GraphQL
