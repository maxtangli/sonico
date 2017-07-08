# symfony source reading

language
- [x] VarDumper 1.3h // dirty magic addressing php defect: var_dump() not so obvious.
- [x] Debug 0.5h // dirty magic addressing php defect: no united exception, tedious debug options.
- PHPUnit Bridge
- Stopwatch 0.1h // measure.
- [x] PropertyAccess 0.5h // dirty magic addressing php defect: no united access grammar.
- [x] PropertyInfo 1h // addressing php defect: reflection not so friendly.
- ClassLoader // deprecated in Symfony 3.3 and it will be removed in 4.0, use composer instead.
- [x] Serializer 0.8h // support json,xml,yaml,csv.
- [x] Filesystem 0.2h // addressing php defect: file api is not exception style.
- [x] Finder 0.8h // COOL! addressing php defect: file api is not powerful for search.
- Process 0.1h // wrap proc_open() for rich features.

config
- [x] OptionsResolver 0.3h // resolve options.
- DependencyInjection
- Config // interface for various config files.
- Dotenv // parse .env file.
- Yaml // parse .yaml file.

feature
- [x] Console 1.7h // console application with rich features.
- [x] Cache 1h // PSR cache implementation.
- [x] EventDispatcher 0.4h// mediator pattern.
- [x] Workflow 0.3h // FSM with event mechanism.

web
- [ ] BrowserKit
- [ ] DomCrawler
- [ ] HttpFoundation
- [ ] HttpKernel
- [ ] Routing
- [ ] Security 0.3h
- Ldap

view
- [ ] Validator 0.5h
- [ ] Form
- [x] Asset 0.5h // dedicated abstractions, browser game use case.
- CssSelector
- [ ] Templating
- [ ] ExpressionLanguage
- [ ] Intl
- [ ] Translation