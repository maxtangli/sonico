# symfony source reading

language
- [x] VarDumper 1.3h // dirty magic addressing php defect: var_dump() not so obvious.
- [x] Debug 0.5h // dirty magic addressing php defect: no united exception, tedious debug options.
- [x] PropertyAccess 0.5h // dirty magic addressing php defect: no united access grammar.
- [x] PropertyInfo 1h // addressing php defect: reflection not so friendly.
- ClassLoader // deprecated in Symfony 3.3 and it will be removed in 4.0, use composer instead.
- [x] Serializer 0.8h // support json,xml,yaml,csv
- [x] Filesystem 0.2h // addressing php defect: file api is not exception style.
- [x] Finder 0.8h // BEAUTIFUL! addressing php defect: file api is not powerful for search.

config
- [x] OptionsResolver 0.3h // resolve options
- Config // interface for various config files
- Dotenv // parse .env
- Yaml // parse .yaml

http
- [ ] BrowserKit
- [ ] DomCrawler
- [ ] HttpFoundation
- [ ] HttpKernel
- [ ] Routing
- Ldap

view
- [ ] Validator
- [ ] Form
- [x] Asset 0.5h // dedicated abstractions, browser game use case.
- [ ] CssSelector
- [ ] Templating
- [ ] ExpressionLanguage
- [ ] Intl
- [ ] Translation

components
- [ ] Console 1.2h // console application with rich features.
- [ ] Process
- [ ] Cache
- [ ] DependencyInjection
- [ ] EventDispatcher
- [ ] Security
- [ ] Stopwatch
- [ ] Workflow
- PHPUnit Bridge