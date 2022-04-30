Database:

- [ ] Project
  - [x] Create      POST /project
  - [x] Update      PATCH /project/{id}
  - [x] Delete      DELETE /project/{id}
    - [ ] Cascade delete for all suites and test cases
  - [x] Get one     GET /project/{id}
  - [x] Get Many    GET /projects

- [x] Test Suites
  - [x] Create      POST /project/{id}/suite
  - [x] Update      PATCH /suite/{id}
  - [x] Delete      DELETE /suite/{id}
    - [ ] Cascade delete all test cases in suite
    - [ ] ...or make test cases orphaned but still belonging to project
  - [x] Get One     GET /suite/{id}
  - [ ] Get all     GET /project/{id}/suites

- [ ] Test Cases
  - [ ] Create      POST /suite/{id}/test
  - [ ] Update      PATCH /test/{id}
  - [ ] Delete      DELETE /test/{id}
  - [ ] Get one     GET /test/{id}
  - [ ] Get all     GET /suite/{id}/tests

Look into:
    - [ ] Nested routers. ex: /project/{id}/suite/{id}/test/{id} == /suite/{id}/test/{id} == /test/{id}
    - [ ] Order of children in one-to-many relationships

New:
- [ ] Alembic
- [ ] GraphQL
