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
- [x] ExpressionLanguage 1.1h // advanced config expression.

feature
- [x] Cache 1h // PSR cache implementation.
- [x] EventDispatcher 0.4h// mediator pattern.
- [x] Workflow 0.3h // FSM with event mechanism.
- [x] Console 1.7h // console application with rich features.

view
- [x] Asset 0.5h // dedicated abstractions, browser game use case.
- DomCrawler 0.1h
- CssSelector
- [x] Validator 0.8h // flexible validation of object.
- Templating 0.1h // a template engine base for twig.
- Intl // i18n
- Translation // i18n
- [ ] Form

web
- BrowserKit 0.1h // a browser simulator support link, form, cookie.
- HttpFoundation 0.1h // http utils e.g. request, response, cookie, file.
- HttpKernel 0.2h // a structured process for converting a Request into a Response by EventDispatcher.
- [x] Routing 0.5h // rich featured route system.
- [ ] Security 0.3h
- Ldap
