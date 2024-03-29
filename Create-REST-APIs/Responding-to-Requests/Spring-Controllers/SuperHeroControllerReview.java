/*

With the annotations we learned in this lesson, we can now:

Map HTTP requests to controllers and methods (@RestController and @RequestMapping)
Specify a path attribute to become a base path (@RequestMapping at the class level)
Declare request types using HTTP method annotations (@GetMapping, @PostMapping, @PutMapping, and @DeleteMapping)
Access request parameters in a method (@RequestParam)
Bind data using template variables (@PathVariable)
Fine-tune the status code returned by a method (@ResponseStatus)
All of these annotations and ResponseStatusException are imported from the org.springframework.web.bind.annotation package.

*/

package com.codecademy.ccapplication;
import java.util.List;
import java.lang.Iterable;
import java.util.Date;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
@RequestMapping("/superHeroes")
public class SuperHeroController {

  private final SuperHeroRepository superHeroRepository;
  private final SuperReportRepository superReportRepository;

  public SuperHeroController(SuperHeroRepository superHeroRepository, SuperReportRepository superReportRepository) {
    this.superHeroRepository = superHeroRepository;
    this.superReportRepository = superReportRepository;
  }

  @GetMapping()
	public Iterable<SuperHero> getSuperHeros() {
    Iterable<SuperHero> superHeroes = superHeroRepository.findAll();
    return superHeroes;
	}

  @PostMapping(path="/addNew")
  public String createNewSuperHero(@RequestParam String firstName, @RequestParam String lastName, @RequestParam String superPower) {
    SuperHero newSuperHero = new SuperHero(firstName, lastName, superPower);
    superHeroRepository.save(newSuperHero);
    return "New Super Hero successfully added!";
  }

  @PostMapping(path="/help")
  public String postHelp(@RequestParam String postalCode, @RequestParam String streetAddress) {
    SuperReport newSuperReport = new SuperReport(postalCode, streetAddress, "");
    superReportRepository.save(newSuperReport);
    return "Thanks! Super Heroes have been dispatched to your location!";
  }

  @GetMapping(path="/heroReport")
  public Iterable<SuperReport> getHeroReport() {
    Iterable<SuperReport> superReport = superReportRepository.findAll();
    return superReport;
  }

  @PostMapping(path="/{postalCode}")
  public Iterable<SuperReport> getHeroReportByPostal(@PathVariable String postalCode) {
    Iterable<SuperReport> superReport = superReportRepository.findByPostalCode(postalCode);
    return superReport;
  }
}
